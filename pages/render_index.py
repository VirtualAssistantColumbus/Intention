from utils.html_ import html
from pages.render_base import render_base


def render_index_a() -> str:
    from app import get_context
    context = get_context()
    
    content = html(f"""
        <!-- UTM Source Tracking Script -->
        <script>
            (function() {{
                const urlParams = new URLSearchParams(window.location.search);
                const utmSource = urlParams.get('utm_source');
                
                if (utmSource) {{
                    document.addEventListener('DOMContentLoaded', function() {{
                        const links = document.querySelectorAll('a[href^="/"], a[href^="./"], a[href^="../"]');
                        links.forEach(link => {{
                            if (link.getAttribute('href').startsWith('#')) return;
                            
                            try {{
                                const url = new URL(link.href, window.location.origin);
                                url.searchParams.set('utm_source', utmSource);
                                link.href = url.toString();
                            }} catch (e) {{
                                const separator = link.href.includes('?') ? '&' : '?';
                                link.href += separator + 'utm_source=' + encodeURIComponent(utmSource);
                            }}
                        }});
                        
                        const forms = document.querySelectorAll('form');
                        forms.forEach(form => {{
                            const existingInput = form.querySelector('input[name="utm_source"]');
                            if (existingInput) {{
                                existingInput.value = utmSource;
                            }} else {{
                                const hiddenInput = document.createElement('input');
                                hiddenInput.type = 'hidden';
                                hiddenInput.name = 'utm_source';
                                hiddenInput.value = utmSource;
                                form.appendChild(hiddenInput);
                            }}
                        }});
                    }});
                }}
            }})();
        </script>

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
            }});
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

        <!-- Section 2: So we're fixing it -->
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
                        name="excitement"
                        placeholder="What's got you excited?"
                        rows="4"
                        class="px-6 py-4 text-xl bg-transparent border-2 border-white text-white placeholder-gray-400 focus:outline-none focus:border-gray-300 transition-colors resize-vertical"
                    ></textarea>
                    <input type="hidden" name="utm_source" value="none">
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
    """)
    
    return render_base(content, "a")