from utils.html import html

def render_base(content: str, version: str = "") -> str:
    return html(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Intention | Waging war against doomscrolling, distractions, and DMs</title>
            
            <!-- Google tag (gtag.js) -->
            <script async src="https://www.googletagmanager.com/gtag/js?id=G-G3RS7R2EE3"></script>
            <script>
                window.dataLayer = window.dataLayer || [];
                function gtag(){{dataLayer.push(arguments);}}
                gtag('js', new Date());
                gtag('config', 'G-G3RS7R2EE3', {{debug_mode: true}});
                
                {f"gtag('set', 'user_properties', {{version_id: '{version}'}});" if version else ""}
            </script>
            
            <script src="https://cdn.tailwindcss.com"></script>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">
            <script src="https://b.kickoffpages.com/2.2.0/kol.js" id="koljs" data-campaign-id="189161" async></script>
            <script>
                tailwind.config = {{
                    theme: {{
                        extend: {{
                            fontFamily: {{
                                'dm-sans': ['DM Sans', 'sans-serif'],
                            }},
                            fontSize: {{
                                'massive': ['128px', '1.1'],
                                'massive-mobile': ['48px', '1.1'],
                            }}
                        }}
                    }}
                }}
            </script>
        </head>
        <body class="bg-black text-white font-dm-sans">
            <div class="min-h-screen">
                {content}
                
                <!-- Navigation Section -->
                <section class="px-8 py-32 md:px-16 lg:px-24 border-t border-gray-800">
                    <div class="text-center">
                        <h2 class="text-4xl md:text-6xl font-bold mb-16 tracking-tight">
                            Explore More
                        </h2>
                        <nav class="flex flex-col sm:flex-row justify-center items-center gap-8 sm:gap-16">
                            <a href="/" class="text-3xl md:text-5xl font-bold tracking-tight hover:text-gray-300 transition-colors">
                                HOME
                            </a>
                            <a href="/mission" class="text-3xl md:text-5xl font-bold tracking-tight hover:text-gray-300 transition-colors">
                                MISSION
                            </a>
                            <a href="/contribute" class="text-3xl md:text-5xl font-bold tracking-tight hover:text-gray-300 transition-colors">
                                CONTRIBUTE
                            </a>
                        </nav>
                    </div>
                </section>
            </div>

            <!-- Custom Source Tracking Script -->
            <script>
                (function() {{
                    const urlParams = new URLSearchParams(window.location.search);
                    const customSource = urlParams.get('custom-source');
                    
                    if (customSource) {{
                        document.addEventListener('DOMContentLoaded', function() {{
                            const links = document.querySelectorAll('a[href^="/"], a[href^="./"], a[href^="../"]');
                            links.forEach(link => {{
                                if (link.getAttribute('href').startsWith('#')) return;
                                
                                try {{
                                    const url = new URL(link.href, window.location.origin);
                                    url.searchParams.set('custom-source', customSource);
                                    link.href = url.toString();
                                }} catch (e) {{
                                    const separator = link.href.includes('?') ? '&' : '?';
                                    link.href += separator + 'custom-source=' + encodeURIComponent(customSource);
                                }}
                            }});
                            
                            const forms = document.querySelectorAll('form');
                            forms.forEach(form => {{
                                const existingInput = form.querySelector('input[name="custom-source"]');
                                if (existingInput) {{
                                    existingInput.value = customSource;
                                }} else {{
                                    const hiddenInput = document.createElement('input');
                                    hiddenInput.type = 'hidden';
                                    hiddenInput.name = 'custom-source';
                                    hiddenInput.value = customSource;
                                    form.appendChild(hiddenInput);
                                }}
                            }});
                        }});
                    }}
                }})();
            </script>
        </body>
        </html>
    """) 