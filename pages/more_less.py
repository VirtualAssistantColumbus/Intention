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
            <div class="max-w-4xl">
                <h1 class="text-massive-mobile md:text-massive font-bold mb-16 leading-none tracking-tight">
                    More/Less
                </h1>
                
                <!-- Headers -->
                <div class="grid grid-cols-2 gap-16 mb-8">
                    <h2 class="text-2xl font-bold">More</h2>
                    <h2 class="text-2xl font-bold">Less</h2>
                </div>
                
                <!-- Rows -->
                <div class="space-y-4">
                    <!-- Row 1: Intention / Autopilot -->
                    <div class="grid grid-cols-2 gap-16">
                        <p class="text-xl">Intention</p>
                        <p class="text-xl">Autopilot</p>
                    </div>
                    
                    <!-- Row 2: Purpose / Apathy -->
                    <div class="grid grid-cols-2 gap-16">
                        <p class="text-xl">Purpose</p>
                        <p class="text-xl">Apathy</p>
                    </div>
                    
                    <!-- Row 3: Discomfort / Ease -->
                    <div class="grid grid-cols-2 gap-16">
                        <p class="text-xl">Discomfort</p>
                        <p class="text-xl">Ease</p>
                    </div>
                    
                    <!-- Row 4: Consequence / Cushion -->
                    <div class="grid grid-cols-2 gap-16">
                        <p class="text-xl">Consequence</p>
                        <p class="text-xl">Cushion</p>
                    </div>
                    
                    <!-- Row 5: Boredom / Stimulation -->
                    <div class="grid grid-cols-2 gap-16">
                        <p class="text-xl">Boredom</p>
                        <p class="text-xl">Stimulation</p>
                    </div>
                    
                    <!-- Row 6: Introspection / (no pair) -->
                    <div class="grid grid-cols-2 gap-16">
                        <p class="text-xl">Introspection</p>
                        <p class="text-xl">Distraction</p>
                    </div>
                    
                    <!-- Row 7: Reflection / (no pair) -->
                    <div class="grid grid-cols-2 gap-16">
                        <p class="text-xl">Reflection</p>
                        <p class="text-xl">Face Value</p>
                    </div>
                    
                    <!-- Row 8: Instinct / Doubt -->
                    <div class="grid grid-cols-2 gap-16">
                        <p class="text-xl">Instinct</p>
                        <p class="text-xl">Doubt</p>
                    </div>
                    
                    <!-- Row 9: Peace / Anxiety -->
                    <div class="grid grid-cols-2 gap-16">
                        <p class="text-xl">Peace</p>
                        <p class="text-xl">Anxiety</p>
                    </div>
                    
                    <!-- Row 10: Agency / Helplessness -->
                    <div class="grid grid-cols-2 gap-16">
                        <p class="text-xl">Agency</p>
                        <p class="text-xl">Helplessness</p>
                    </div>
                    
                    <!-- Row 11: Influence / Worry -->
                    <div class="grid grid-cols-2 gap-16">
                        <p class="text-xl">Influence</p>
                        <p class="text-xl">Worry</p>
                    </div>
                    
                    <!-- Row 12: Substance / Ceremony -->
                    <div class="grid grid-cols-2 gap-16">
                        <p class="text-xl">Substance</p>
                        <p class="text-xl">Ceremony</p>
                    </div>
                    
                    <!-- Row 13: Connection / Cheap Substitutes -->
                    <div class="grid grid-cols-2 gap-16">
                        <p class="text-xl">Connection</p>
                        <p class="text-xl">Cheap Substitutes</p>
                    </div>
                    
                    <!-- Row 14: Integrative Thinking / Reductionism -->
                    <div class="grid grid-cols-2 gap-16">
                        <p class="text-xl">Holistic</p>
                        <p class="text-xl">Reductionist</p>
                    </div>
                    
                    <!-- Row 15: Contrast / Constant -->
                    <div class="grid grid-cols-2 gap-16">
                        <p class="text-xl">Contrast</p>
                        <p class="text-xl">Constant</p>
                    </div>
                    
                    <!-- Row 16: Discovery / Learning -->
                    <div class="grid grid-cols-2 gap-16">
                        <p class="text-xl">Discovery</p>
                        <p class="text-xl">Learning</p>
                    </div>
                    
                    <!-- Row 17: Clarity / Clutter -->
                    <div class="grid grid-cols-2 gap-16">
                        <p class="text-xl">Clarity</p>
                        <p class="text-xl">Clutter</p>
                    </div>
                    
                    <!-- Row 18: Wonder / Indifference -->
                    <div class="grid grid-cols-2 gap-16">
                        <p class="text-xl">Wonder</p>
                        <p class="text-xl">Indifference</p>
                    </div>
                </div>
            </div>
        </section>
                   
        { nav() }
    """)
    
    return base(content)