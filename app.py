from flask import Flask, request, g
from dataclasses import dataclass
from enum import StrEnum
import os

# Import render functions
from pages.render_index import render_index_a
from pages.render_mission import render_mission
from pages.render_contribute import render_contribute
from pages.render_status import render_status

class Version(StrEnum):
    A = "a"  # basic
    # B = "b"  # enhanced - When ready

@dataclass
class RequestContext:
    version: Version = Version.A
    update_cookie: bool = False

def set_context(version: Version, update_cookie: bool = False) -> None:
    g._context = RequestContext(version=version, update_cookie=update_cookie)

def get_context() -> RequestContext:
    if not hasattr(g, '_context'):
        g._context = RequestContext()
    return g._context

def create_app():
    app = Flask(__name__, static_folder='static')
    
    @app.before_request
    def assign_version():
        # Check if we're forcing a version change
        force_version = request.args.get('force_version')
        if force_version and force_version in Version:
            set_context(version=Version(force_version), update_cookie=True)
        else:
            existing_version = request.cookies.get('version_id', Version.A)
            try:
                version = Version(existing_version)
            except ValueError:
                version = Version.A  # fallback for invalid cookie values
            set_context(version=version, update_cookie=False)

    @app.after_request  
    def set_version_cookie(response):
        # Set cookie if user doesn't have one OR if we're forcing an update
        context = get_context()
        if not request.cookies.get('version_id') or context.update_cookie:
            response.set_cookie('version_id', context.version, 
                              max_age=60*60*24*90,  # 90 days
                              secure=True,  # Use if HTTPS
                              samesite='Lax')
        return response
    
    @app.route('/')
    def index():
        context = get_context()
        
        if context.version == Version.A:
            return render_index_a()
        # elif context.version == Version.B:
        #     return render_index_b()
        else:
            return render_index_a()  # fallback
    
    @app.route('/mission')
    def mission():
        context = get_context()
        return render_mission(context.version)
    
    @app.route('/contribute')
    def contribute():
        context = get_context()
        return render_contribute(context.version)
    
    @app.route('/status')
    def status():
        context = get_context()
        return render_status(context.version)
    
    return app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)