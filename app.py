import os

from flask import Flask, request

from request_context import Version, get_context, set_context
from shared_dependencies import shared, route_registry

#TODO:
# - How to preserve UTM source when the user changes pages. (This is only relevant if we want the utm source captured in KickoffLabs form). Not necessary.

def create_app():
    # Initialize the environment
    shared.environment
    
    web_app = Flask(__name__, static_folder='static')

    @web_app.before_request
    def assign_version():
        # Check if we're forcing a version change
        force_version = request.args.get('force_version')
        # Get utm_source from query parameters
        utm_source = request.args.get('utm_source', '')
        
        if force_version and force_version in Version:
            set_context(version=Version(force_version), update_cookie=True, utm_source=utm_source)
        else:
            existing_version = request.cookies.get('version_id', Version.A)
            try:
                version = Version(existing_version)
            except ValueError:
                version = Version.A  # fallback for invalid cookie values
            set_context(version=version, update_cookie=False, utm_source=utm_source)

    @web_app.after_request  
    def set_version_cookie(response):
        # Set cookie if user doesn't have one OR if we're forcing an update
        context = get_context()
        if not request.cookies.get('version_id') or context.update_cookie:
            response.set_cookie('version_id', context.version, 
                              max_age=60*60*24*90,  # 90 days
                              secure=True,  # Use if HTTPS
                              samesite='Lax')
        return response
    
    # Import all pages to trigger route registration
    import pages.render_index
    import pages.render_scroll_interrupt_letter  
    import pages.render_mission
    import pages.render_contribute
    import pages.render_status
    import pages.render_enddoomscrolling_letter
    
    # Apply all registered routes to the Flask app
    route_registry.apply_routes(web_app)
    
    return web_app

web_app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    web_app.run(host='0.0.0.0', port=port, debug=True)