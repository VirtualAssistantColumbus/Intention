from utils.html_ import html
from pages.render_base import render_base
from shared_dependencies import route

@route('/status')
def render_status() -> str:
    from request_context import get_context
    context = get_context()
    version = context.version
    
    content = html(f"""
        <!-- Status Header -->
        <section class="px-8 py-32 md:px-16 lg:px-24">
            <h1 class="text-massive-mobile md:text-massive font-bold mb-16 leading-none tracking-tight">
                You're in.
            </h1>
            
            <!-- Waitlist Status Embed -->
            <div class="max-w-2xl">
                <div data-kol-snippet="embedpage" data-kolPageId="398605" class="kol-embed-page-frame default"></div>
            </div>
        </section>
    """)
    
    return render_base(content) 