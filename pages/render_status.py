from utils.html import html
from pages.render_base import render_base

def render_status(version: str) -> str:
    content = html(f"""
        <!-- Status Header -->
        <section class="px-8 py-32 md:px-16 lg:px-24">
            <h1 class="text-massive-mobile md:text-massive font-bold mb-16 leading-none tracking-tight">
                You're in.
            </h1>
            <div class="max-w-4xl space-y-8">
                <p class="text-3xl md:text-5xl font-medium leading-tight">
                    Welcome to the movement for intentional technology.
                </p>
            </div>
        </section>

        <!-- Waitlist Status -->
        <section class="px-8 py-32 md:px-16 lg:px-24">
            <h2 class="text-4xl md:text-6xl font-bold mb-16 leading-none tracking-tight">
                Your Status
            </h2>
            <div class="max-w-4xl space-y-8 mb-16">
                <p class="text-2xl md:text-4xl font-medium leading-tight">
                    Check your position on the waitlist and track our progress.
                </p>
            </div>
            
            <!-- Waitlist Status Embed Placeholder -->
            <div class="max-w-2xl">
                <div data-kol-snippet="embedpage" data-kolPageId="398605" class="kol-embed-page-frame default"></div>
            </div>
        </section>

        <!-- What's Next -->
        <section class="px-8 py-32 md:px-16 lg:px-24">
            <h2 class="text-4xl md:text-6xl font-bold mb-16 leading-none tracking-tight">
                What's Next?
            </h2>
            <div class="max-w-4xl space-y-12">
                <div class="space-y-6">
                    <h3 class="text-3xl md:text-4xl font-bold">Stay Connected</h3>
                    <p class="text-xl md:text-2xl leading-relaxed">
                        We'll send you updates as we build the platform, including exclusive previews and early access opportunities.
                    </p>
                </div>
                
                <div class="space-y-6">
                    <h3 class="text-3xl md:text-4xl font-bold">Spread the Word</h3>
                    <p class="text-xl md:text-2xl leading-relaxed">
                        Share our mission with friends and family who are tired of addictive social media. Every person who joins strengthens our movement.
                    </p>
                </div>
                
                <div class="space-y-6">
                    <h3 class="text-3xl md:text-4xl font-bold">Get Involved</h3>
                    <p class="text-xl md:text-2xl leading-relaxed">
                        Ready to do more than wait? Check out ways you can actively contribute to building the future of social media.
                    </p>
                    <a href="/contribute" class="inline-block px-8 py-4 text-xl border-2 border-white text-white font-medium hover:bg-white hover:text-black transition-colors">
                        Learn More
                    </a>
                </div>
            </div>
        </section>

        <!-- Progress Updates -->
        <section class="px-8 py-32 md:px-16 lg:px-24">
            <h2 class="text-4xl md:text-6xl font-bold mb-16 leading-none tracking-tight">
                Our Progress
            </h2>
            <div class="max-w-4xl space-y-8">
                <p class="text-2xl md:text-4xl font-medium leading-tight">
                    We're building in the open. Here's what we're working on:
                </p>
                <div class="grid md:grid-cols-3 gap-8 mt-16">
                    <div class="space-y-4">
                        <div class="text-4xl font-bold text-gray-400">01</div>
                        <h3 class="text-2xl font-bold">Platform Design</h3>
                        <p class="text-lg leading-relaxed">
                            Creating user experiences that prioritize well-being over engagement metrics.
                        </p>
                    </div>
                    <div class="space-y-4">
                        <div class="text-4xl font-bold text-gray-400">02</div>
                        <h3 class="text-2xl font-bold">Core Features</h3>
                        <p class="text-lg leading-relaxed">
                            Building the essential tools for meaningful connection without the distractions.
                        </p>
                    </div>
                    <div class="space-y-4">
                        <div class="text-4xl font-bold text-gray-400">03</div>
                        <h3 class="text-2xl font-bold">Beta Testing</h3>
                        <p class="text-lg leading-relaxed">
                            Getting feedback from our community to ensure we're building something valuable.
                        </p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Thank You -->
        <section class="px-8 py-32 md:px-16 lg:px-24">
            <div class="max-w-4xl space-y-8 text-center">
                <h2 class="text-4xl md:text-6xl font-bold mb-16 leading-none tracking-tight">
                    Thank You
                </h2>
                <p class="text-2xl md:text-4xl font-medium leading-tight">
                    For believing in a better future for technology.
                </p>
                <p class="text-2xl md:text-4xl font-medium leading-tight">
                    Together, we're going to make it happen.
                </p>
            </div>
        </section>
    """)
    
    return render_base(content, version) 