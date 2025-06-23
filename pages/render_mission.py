from utils.html_ import html
from pages.render_base import render_base

def render_mission(version: str) -> str:
    content = html(f"""
        <!-- Mission Header -->
        <section class="px-8 py-32 md:px-16 lg:px-24">
            <h1 class="text-massive-mobile md:text-massive font-bold mb-16 leading-none tracking-tight">
                Our Mission
            </h1>
            <div class="max-w-4xl space-y-8">
                <p class="text-3xl md:text-5xl font-medium leading-tight">
                    We're building technology that serves humanity, not the other way around.
                </p>
            </div>
        </section>

        <!-- The Problem -->
        <section class="px-8 py-32 md:px-16 lg:px-24">
            <h2 class="text-4xl md:text-6xl font-bold mb-16 leading-none tracking-tight">
                The Problem
            </h2>
            <div class="max-w-4xl space-y-8">
                <p class="text-2xl md:text-4xl font-medium leading-tight">
                    Social media platforms are designed to capture and monetize your attention.
                </p>
                <p class="text-2xl md:text-4xl font-medium leading-tight">
                    Infinite scroll, push notifications, and algorithmic feeds keep you engaged far longer than intended.
                </p>
                <p class="text-2xl md:text-4xl font-medium leading-tight">
                    This leaves less time for meaningful relationships, creative pursuits, and personal growth.
                </p>
            </div>
        </section>

        <!-- Our Solution -->
        <section class="px-8 py-32 md:px-16 lg:px-24">
            <h2 class="text-4xl md:text-6xl font-bold mb-16 leading-none tracking-tight">
                Our Solution
            </h2>
            <div class="max-w-4xl space-y-8">
                <p class="text-2xl md:text-4xl font-medium leading-tight">
                    We're reimagining social media to prioritize your well-being over engagement metrics.
                </p>
                <p class="text-2xl md:text-4xl font-medium leading-tight">
                    No infinite scroll. No algorithmic manipulation. No attention hijacking.
                </p>
                <p class="text-2xl md:text-4xl font-medium leading-tight">
                    Just the tools you need to stay connected with what matters most.
                </p>
            </div>
        </section>

        <!-- Our Values -->
        <section class="px-8 py-32 md:px-16 lg:px-24">
            <h2 class="text-4xl md:text-6xl font-bold mb-16 leading-none tracking-tight">
                Our Values
            </h2>
            <div class="max-w-4xl space-y-12">
                <div class="space-y-4">
                    <h3 class="text-2xl md:text-3xl font-bold">Intentional Design</h3>
                    <p class="text-xl md:text-2xl leading-relaxed">
                        Every feature serves a clear purpose in helping you connect meaningfully, not just frequently.
                    </p>
                </div>
                <div class="space-y-4">
                    <h3 class="text-2xl md:text-3xl font-bold">Transparency</h3>
                    <p class="text-xl md:text-2xl leading-relaxed">
                        You should always know how and why content is shown to you. No hidden algorithms.
                    </p>
                </div>
                <div class="space-y-4">
                    <h3 class="text-2xl md:text-3xl font-bold">User Control</h3>
                    <p class="text-xl md:text-2xl leading-relaxed">
                        You decide what you see, when you see it, and how much time you spend online.
                    </p>
                </div>
                <div class="space-y-4">
                    <h3 class="text-2xl md:text-3xl font-bold">Privacy First</h3>
                    <p class="text-xl md:text-2xl leading-relaxed">
                        Your data belongs to you. We never sell it, and we only collect what's necessary.
                    </p>
                </div>
            </div>
        </section>

        <!-- Join Our Mission -->
        <section class="px-8 py-32 md:px-16 lg:px-24">
            <h2 class="text-4xl md:text-6xl font-bold mb-16 leading-none tracking-tight">
                Join Our Mission
            </h2>
            <div class="max-w-4xl space-y-8 mb-16">
                <p class="text-2xl md:text-4xl font-medium leading-tight">
                    Together, we can build a better internet that serves humanity's best interests.
                </p>
                <p class="text-2xl md:text-4xl font-medium leading-tight">
                    Join us in creating technology that enhances life rather than consuming it.
                </p>
            </div>
            
            <!-- Call to Action -->
            <div class="flex flex-col sm:flex-row gap-6">
                <a href="/" class="px-8 py-4 text-xl bg-white text-black font-medium hover:bg-gray-200 transition-colors text-center">
                    Sign Up for Updates
                </a>
                <a href="/contribute" class="px-8 py-4 text-xl border-2 border-white text-white font-medium hover:bg-white hover:text-black transition-colors text-center">
                    Get Involved
                </a>
            </div>
        </section>
    """)
    
    return render_base(content) 