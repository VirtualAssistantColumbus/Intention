from components.nav import nav
from utils.html_ import html
from components.base import base
from components.social_proof import social_proof
from shared_dependencies import route

@route('/team')
def team() -> str:
    from request_context import get_context
    context = get_context()
    version = context.version
    
    content = html(f"""
        <!-- Team Header -->
        <section class="px-8 py-32 md:px-16 lg:px-24">
            <div class="max-w-4xl space-y-8">
                <p class="text-3xl md:text-5xl font-medium leading-tight">
                    We're a group of optimists that believe technology and humanity can, and must, coexist.
                </p>
            </div>
        </section>

        <!-- Team Members -->
        <section class="px-8 md:px-16 lg:px-24">
            <div class="max-w-6xl">
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-16">
                    
                    <!-- Team Member 1 -->
                    <div class="text-center space-y-6">
                        <div class="w-64 h-64 mx-auto bg-gray-800 rounded-full flex items-center justify-center">
                            <img src="/static/team/ray.jpg" alt="Ray Li" class="w-full h-full object-cover rounded-full">
                        </div>
                        <div class="space-y-2">
                            <h3 class="text-2xl md:text-3xl font-bold">Ray Li</h3>
                            <p class="text-lg md:text-xl text-gray-300">Founder</p>
                        </div>
                    </div>
                    
                </div>
            </div>
        </section>

        <!-- Community Section -->
        <section class="px-8 py-32 md:px-16 lg:px-24">
            <div class="max-w-4xl space-y-16">
                <p class="text-3xl md:text-5xl font-medium leading-tight">
                    Powered by a community of people who are choosing to live intentionally and take their lives back from technology.
                </p>
                
                <!-- Social Proof Carousel -->
                <div class="space-y-8">
                    {social_proof()}
                </div>
            </div>
        </section>
                   
        { nav() }
    """)
    
    return base(content) 