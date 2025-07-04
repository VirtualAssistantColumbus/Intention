from utils.html_ import html
from shared_dependencies import shared

def base(content: str) -> str:
    from app import get_context
    context = get_context()
    
    debug_mode = "true" if shared.environment.gtag_debug_mode else "false"
    
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
                gtag('config', 'G-G3RS7R2EE3', {{debug_mode: {debug_mode}}});
                
                {f"gtag('set', 'user_properties', {{version_id: '{context.version}'}});" if context.version else ""}
            </script>
            
            <!-- Meta Pixel Code -->
            <script>!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js'); fbq('init', '1092345086106557'); fbq('track', 'PageView');</script><noscript> <img height="1" width="1" src="https://www.facebook.com/tr?id=1092345086106557&ev=PageView&noscript=1"/></noscript>
            <!-- End Meta Pixel Code -->

            <!-- LinkedIn Ads Code -->
            <script type="text/javascript">
                _linkedin_partner_id = "7401132";
                window._linkedin_data_partner_ids = window._linkedin_data_partner_ids || [];
                window._linkedin_data_partner_ids.push(_linkedin_partner_id);
            </script>
            <script type="text/javascript">
                (function(l) {{if (!l){{window.lintrk = function(a,b){{window.lintrk.q.push([a,b])}};window.lintrk.q=[]}}var s = document.getElementsByTagName("script")[0];var b = document.createElement("script");b.type = "text/javascript";b.async = true;b.src = "https://snap.licdn.com/li.lms-analytics/insight.min.js";s.parentNode.insertBefore(b, s);}})(window.lintrk);
            </script>
            <noscript>
                <img height="1" width="1" style="display:none;" alt="" src="https://px.ads.linkedin.com/collect/?pid=7401132&fmt=gif" />
            </noscript>
            <!-- End LinkedIn Ads Code -->

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
            
            {f'''
            <!-- UTM Source Preservation Script -->
            <script>
                (function() {{
                    const utmSource = "{context.utm_source}";
                    
                    if (utmSource) {{
                        // Add utm_source to current URL if not already present
                        const currentUrl = new URL(window.location);
                        if (!currentUrl.searchParams.has('utm_source')) {{
                            currentUrl.searchParams.set('utm_source', utmSource);
                            window.history.replaceState(null, '', currentUrl.toString());
                        }}
                        
                        // Wait for DOM to be ready
                        document.addEventListener('DOMContentLoaded', function() {{
                            // Update all internal links
                            const links = document.querySelectorAll('a[href^="/"], a[href^="./"], a[href^="../"]');
                            links.forEach(link => {{
                                if (link.getAttribute('href').startsWith('#')) return;
                                
                                try {{
                                    const url = new URL(link.href, window.location.origin);
                                    if (!url.searchParams.has('utm_source')) {{
                                        url.searchParams.set('utm_source', utmSource);
                                        link.href = url.toString();
                                    }}
                                }} catch (e) {{
                                    const separator = link.href.includes('?') ? '&' : '?';
                                    if (!link.href.includes('utm_source=')) {{
                                        link.href += separator + 'utm_source=' + encodeURIComponent(utmSource);
                                    }}
                                }}
                            }});
                            
                            // Update all forms with hidden utm_source input
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
            ''' if context.utm_source else ""}
        </head>
        <body class="bg-black text-white font-dm-sans">
            <div class="min-h-screen">
                {content}
                
                <!-- Navigation Section (Hidden)
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
                -->
            </div>
        </body>
        </html>
    """) 