from utils.html_ import html
from components.render_base import render_base
from components.render_nav import render_nav
from shared_dependencies import route
from request_context import Version


@route('/')
def index() -> str:
    from request_context import get_context
    context = get_context()
    
    if context.version == Version.A:
        return render_index_a()
    # elif context.version == Version.B:
    #     return render_index_b()
    else:
        return render_index_a()  # fallback

def render_index_a() -> str:
    from request_context import get_context
    context = get_context()
    
    content = html(f"""
        <!-- Form Submission Tracking Script -->
        <script>
            document.addEventListener('DOMContentLoaded', function() {{
                const form = document.querySelector('form');
                if (form) {{
                    form.addEventListener('submit', function(e) {{
                        // Track form submission with gtag
                        if (typeof gtag !== 'undefined') {{
                            gtag('event', 'form_submit', {{
                                'event_category': 'engagement',
                                'event_label': 'join_waitlist'
                            }});
                        }}
                    }});
                }}
            }}
        </script>

        <!-- Section 1: Social media is broken -->
        <section class="px-8 py-32 md:px-16 lg:px-24">
            <h1 class="text-massive-mobile md:text-massive font-bold mb-16 leading-none tracking-tight">
                Social media is broken.
            </h1>
            <div class="max-w-4xl space-y-8">
                <p class="text-3xl md:text-5xl font-medium leading-tight">
                    Your apps are designed to be addictive.
                </p>
                <p class="text-3xl md:text-5xl font-medium leading-tight">
                    Keeping you glued to your screen and distracting you from the things that truly matter in life.
                </p>
            </div>
        </section>

        <!-- Section 2: Fixing it -->
        <section class="px-8 py-32 md:px-16 lg:px-24">
            <h1 class="text-massive-mobile md:text-massive font-bold mb-16 leading-none tracking-tight">
                So we're fixing it.
            </h1>
            <div class="max-w-4xl space-y-8">
                <p class="text-3xl md:text-5xl font-medium leading-tight">
                    We're taking the apps you love to hate and ripping out everything that doesn't need to be there.
                </p>
                <p class="text-3xl md:text-5xl font-medium leading-tight">
                    So you can stay connected without the distractions.
                </p>
            </div>
        </section>

        <!-- Section 3: Join us -->
        <section class="px-8 py-32 md:px-16 lg:px-24">
            <h1 class="text-massive-mobile md:text-massive font-bold mb-16 leading-none tracking-tight">
                Join us.
            </h1>
            <div class="max-w-4xl space-y-8 mb-16">
                <p class="text-3xl md:text-5xl font-medium leading-tight">
                    We're on a mission to make technology serve humanity again.
                </p>
                <p class="text-3xl md:text-5xl font-medium leading-tight">
                    Sign up to know when we launch.
                </p>
            </div>
            
            <!-- Intake Form -->
            <form class="max-w-2xl">
                <div class="flex flex-col gap-4">
                    <input 
                        name="email"
                        type="email" 
                        placeholder="Enter your email"
                        class="px-6 py-4 text-xl bg-transparent border-2 border-white text-white placeholder-gray-400 focus:outline-none focus:border-gray-300 transition-colors"
                        required
                    >
                    <textarea 
                        name="comments"
                        placeholder="What social media platform do you want us to fix first? Leave any comments or suggestions here! (optional)"
                        rows="4"
                        class="px-6 py-4 text-xl bg-transparent border-2 border-white text-white placeholder-gray-400 focus:outline-none focus:border-gray-300 transition-colors resize-vertical"
                    ></textarea>
                    <input type="hidden" name="utm_source" value="{context.utm_source or 'none'}">
                    <input type="hidden" name="version" value="{context.version}">
                    <button 
                        type="submit"
                        class="px-8 py-4 text-xl bg-white text-black font-medium hover:bg-gray-200 transition-colors"
                    >
                        Join
                    </button>
                </div>
            </form>
        </section>
        { render_nav() }
    """)
    
    return render_base(content)