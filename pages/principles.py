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
                    <h2 class="text-2xl md:text-3xl font-bold">Mission Statement</h2>
                    <p class="text-xl md:text-2xl leading-relaxed">
                        We exist to salvage the human spirit from the modern world—to protect it, nurture it, and empower it to thrive in this world—and then also to change the world so that it is serves rather than attacks our human sensibilities.
                    </p>
                    <p class="text-xl md:text-2xl leading-relaxed">
                        We're doing this by creating apps that make a statement about how technology should be build. Apps that honor and respect your attention. Apps that empower you to do exactly what you intend to do—nothing more and nothing less. Apps that get out of your way and eliminate distractions.
                    </p>
                </div>
                
                <div class="space-y-8">
                    <h2 class="text-2xl md:text-3xl font-bold">Our Principles</h2>
                    <div class="space-y-6 ml-8">
                        <p class="text-xl md:text-2xl leading-relaxed">
                            <span class="font-black text-white text-lg mr-3">1.</span>
                            Nothing should take your attention without your consent.
                        </p>
                        <p class="text-xl md:text-2xl leading-relaxed">
                            <span class="font-black text-white text-lg mr-3">2.</span>
                            You should control your devices, they shouldn't control you.
                        </p>
                        <p class="text-xl md:text-2xl leading-relaxed">
                            <span class="font-black text-white text-lg mr-3">3.</span>
                            People are capable of, and should, manage themselves. You don't need an app that runs your life. You need your apps to get out of your way.
                        </p>
                    </div>
                </div>
            </div>
        </section>
                   
        { nav() }
    """)
    
    return base(content) 