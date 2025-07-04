from components.nav import nav
from utils.html_ import html
from components.base import base
from shared_dependencies import route

@route('/principles')
def principles() -> str:
    from request_context import get_context
    context = get_context()
    version = context.version
    
    content = html(f"""
        <section class="px-8 py-32 md:px-16 lg:px-24">
            <div class="max-w-4xl space-y-16">
                <div class="space-y-8">
                    <h2 class="text-2xl md:text-3xl font-bold">Our Principles</h2>
                </div>
                
                <div class="space-y-12">
                    <div class="space-y-6">
                        <h3 class="text-xl md:text-2xl font-bold text-white">Design</h3>
                        <div class="space-y-4 ml-8">
                            <div class="flex items-start space-x-3">
                                <span class="font-black text-white text-lg flex-shrink-0 min-w-[2rem]">1.</span>
                                <p class="text-lg md:text-xl leading-relaxed">
                                    Nothing should take your attention without your consent.
                                </p>
                            </div>
                            <div class="flex items-start space-x-3">
                                <span class="font-black text-white text-lg flex-shrink-0 min-w-[2rem]">2.</span>
                                <p class="text-lg md:text-xl leading-relaxed">
                                    You should control your devices, they shouldn't control you.
                                </p>
                            </div>
                            <div class="flex items-start space-x-3">
                                <span class="font-black text-white text-lg flex-shrink-0 min-w-[2rem]">3.</span>
                                <p class="text-lg md:text-xl leading-relaxed">
                                    People can and should manage themselves. You don't need an app to run your life. You need your apps to get out of your way.
                                </p>
                            </div>
                        </div>
                    </div>
                    
                    <div class="space-y-6">
                        <h3 class="text-xl md:text-2xl font-bold text-white">Mode</h3>
                        <div class="space-y-4 ml-8">
                            <div class="flex items-start space-x-3">
                                <span class="font-black text-white text-lg flex-shrink-0 min-w-[2rem]">1.</span>
                                <div class="flex-1">
                                    <p class="text-lg md:text-xl leading-relaxed cursor-pointer hover:text-white transition-colors principle-item" data-expandable="true">
                                        Attack the problem, not the person.
                                    </p>
                                    <div class="principle-context overflow-hidden transition-all duration-300 ease-out" style="max-height: 0; opacity: 0;">
                                        <p class="text-white text-base md:text-lg leading-relaxed mt-4">
                                            The problems that face this world are complex, and it is not our role to assign blame. We believe that most technologies were created with good intentions. We all share the responsibility for where we are, and we all must step up to fix it.
                                        </p>
                                    </div>
                                </div>
                            </div>
                            <div class="flex items-start space-x-3">
                                <span class="font-black text-white text-lg flex-shrink-0 min-w-[2rem]">2.</span>
                                <div class="flex-1">
                                    <p class="text-lg md:text-xl leading-relaxed cursor-pointer hover:text-white transition-colors principle-item" data-expandable="true">
                                        If something is important enough, there is no room to execute it perfectly.
                                    </p>
                                    <div class="principle-context overflow-hidden transition-all duration-300 ease-out" style="max-height: 0; opacity: 0;">
                                        <p class="text-white text-base md:text-lg leading-relaxed mt-4">
                                            If someone were dying in front of you, would you pause because you hadn't learned CPR? Or would you jump into action?
                                        </p>
                                    </div>
                                </div>
                            </div>
                            <div class="flex items-start space-x-3">
                                <span class="font-black text-white text-lg flex-shrink-0 min-w-[2rem]">3.</span>
                                <p class="text-lg md:text-xl leading-relaxed">
                                    Stories are more useful than statistics.
                                </p>
                            </div>
                        </div>
                    </div>
                    
                    <div class="space-y-6">
                        <h3 class="text-xl md:text-2xl font-bold text-white">Philosophy</h3>
                        <div class="space-y-4 ml-8">
                            <div class="flex items-start space-x-3">
                                <span class="font-black text-white text-lg flex-shrink-0 min-w-[2rem]">1.</span>
                                <p class="text-lg md:text-xl leading-relaxed">
                                    The most important truths are self-evident.
                                </p>
                            </div>
                            <div class="flex items-start space-x-3">
                                <span class="font-black text-white text-lg flex-shrink-0 min-w-[2rem]">2.</span>
                                <p class="text-lg md:text-xl leading-relaxed">
                                    "Man is not in search of happiness but a reason to be happy." -Viktor Frankl
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        
        <script>
            document.addEventListener('DOMContentLoaded', function() {{
                const principleItems = document.querySelectorAll('.principle-item[data-expandable="true"]');
                
                principleItems.forEach(item => {{
                    item.addEventListener('click', function() {{
                        const context = item.nextElementSibling;
                        if (context && context.classList.contains('principle-context')) {{
                            const isExpanded = context.style.maxHeight !== '0px' && context.style.maxHeight !== '';
                            
                            if (isExpanded) {{
                                // Collapse
                                context.style.maxHeight = '0px';
                                context.style.opacity = '0';
                            }} else {{
                                // Expand
                                context.style.maxHeight = context.scrollHeight + 'px';
                                context.style.opacity = '1';
                            }}
                        }}
                    }});
                }});
            }});
        </script>
                   
        {nav()}
    """)
    
    return base(content) 