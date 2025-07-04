from components.nav import nav
from utils.html_ import html
from components.base import base
from shared_dependencies import route

@route('/mission')
def mission() -> str:
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
                        We're doing this by creating apps that make a statement about how technology should be build. Apps that honor and respect your attention. Apps without distractions that get out of your way. Apps that empower you to live your best life.
                    </p>
                </div>
            </div>
        </section>
                   
        { nav() }
    """)
    
    return base(content) 