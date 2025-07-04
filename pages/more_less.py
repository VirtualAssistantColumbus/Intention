from components.nav import nav
from utils.html_ import html
from components.base import base
from shared_dependencies import route

@route('/more-less')
def more_less() -> str:
    from request_context import get_context
    context = get_context()
    
    content = html(f"""
        <section class="px-8 py-32 md:px-16 lg:px-24">
            <div class="max-w-6xl mx-auto">
                <h1 class="text-massive-mobile md:text-massive font-bold mb-16 leading-none tracking-tight text-center">
                    More/Less
                </h1>
                
                <div class="space-y-16">
                    <!-- Introduction -->
                    <div class="text-center max-w-4xl mx-auto">
                        <p class="text-2xl md:text-3xl font-medium leading-tight">
                            What we need more of, and what we need less of.
                        </p>
                    </div>
                    
                    <!-- More/Less Grid -->
                    <div class="space-y-12">
                        <!-- Row 1: More intention, less automatic -->
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-start">
                            <div class="text-center md:text-right">
                                <div class="text-3xl md:text-4xl font-bold text-green-400 mb-2">
                                    More
                                </div>
                                <div class="text-xl md:text-2xl font-medium">
                                    Intention
                                </div>
                            </div>
                            <div class="text-center md:text-left">
                                <div class="text-3xl md:text-4xl font-bold text-red-400 mb-2">
                                    Less
                                </div>
                                <div class="text-xl md:text-2xl font-medium">
                                    Automatic
                                </div>
                            </div>
                        </div>
                        
                        <!-- Row 2: More purpose, less apathy -->
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-start">
                            <div class="text-center md:text-right">
                                <div class="text-3xl md:text-4xl font-bold text-green-400 mb-2">
                                    More
                                </div>
                                <div class="text-xl md:text-2xl font-medium">
                                    Purpose
                                </div>
                            </div>
                            <div class="text-center md:text-left">
                                <div class="text-3xl md:text-4xl font-bold text-red-400 mb-2">
                                    Less
                                </div>
                                <div class="text-xl md:text-2xl font-medium">
                                    Apathy
                                </div>
                            </div>
                        </div>
                        
                        <!-- Row 3: More discomfort (no pair) -->
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-start">
                            <div class="text-center md:text-right">
                                <div class="text-3xl md:text-4xl font-bold text-green-400 mb-2">
                                    More
                                </div>
                                <div class="text-xl md:text-2xl font-medium">
                                    Discomfort
                                </div>
                            </div>
                            <div class="text-center md:text-left opacity-40">
                                <div class="text-xl md:text-2xl font-medium italic">
                                    —
                                </div>
                            </div>
                        </div>
                        
                        <!-- Row 4: More consequence, less cushion -->
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-start">
                            <div class="text-center md:text-right">
                                <div class="text-3xl md:text-4xl font-bold text-green-400 mb-2">
                                    More
                                </div>
                                <div class="text-xl md:text-2xl font-medium">
                                    Consequence
                                </div>
                            </div>
                            <div class="text-center md:text-left">
                                <div class="text-3xl md:text-4xl font-bold text-red-400 mb-2">
                                    Less
                                </div>
                                <div class="text-xl md:text-2xl font-medium">
                                    Cushion
                                </div>
                            </div>
                        </div>
                        
                        <!-- Add more rows as needed -->
                        
                    </div>
                    
                    <!-- Optional: Add a note about the philosophy -->
                    <div class="text-center max-w-4xl mx-auto pt-16 border-t border-gray-700">
                        <p class="text-lg md:text-xl leading-relaxed opacity-80">
                            Sometimes growth requires embracing what feels uncomfortable, 
                            choosing deliberate action over passive consumption, 
                            and accepting the natural consequences of our choices.
                        </p>
                    </div>
                </div>
            </div>
        </section>
                   
        { nav() }
    """)
    
    return base(content) 