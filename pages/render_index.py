from utils.html_ import html
from pages.render_base import render_base

def render_index_a() -> str:
    content = html(f"""
        <!-- Section 1: Social media is broken -->
        <section class="px-8 py-32 md:px-16 lg:px-24">
            <h1 class="text-massive-mobile md:text-massive font-bold mb-16 leading-none tracking-tight">
                Social media is broken.
            </h1>
            <div class="max-w-4xl space-y-8">
                <p class="text-3xl md:text-5xl font-medium leading-tight">
                    Your apps are designed to be addictive.
                </p>
                <p class="text-3xl md:text-5xl font-medium leading-tight">
                    Keeping you glued to your screen and distracting you from the things that truly matter in life.
                </p>
            </div>
        </section>

        <!-- Section 2: So we're fixing it -->
        <section class="px-8 py-32 md:px-16 lg:px-24">
            <h1 class="text-massive-mobile md:text-massive font-bold mb-16 leading-none tracking-tight">
                So we're fixing it.
            </h1>
            <div class="max-w-4xl space-y-8">
                <p class="text-3xl md:text-5xl font-medium leading-tight">
                    We're taking the apps you love to hate and ripping out everything that doesn't need to be there.
                </p>
                <p class="text-3xl md:text-5xl font-medium leading-tight">
                    So you can stay connected without the distractions.
                </p>
            </div>
        </section>

        <!-- Section 3: Join us -->
        <section class="px-8 py-32 md:px-16 lg:px-24">
            <h1 class="text-massive-mobile md:text-massive font-bold mb-16 leading-none tracking-tight">
                Join us.
            </h1>
            <div class="max-w-4xl space-y-8 mb-16">
                <p class="text-3xl md:text-5xl font-medium leading-tight">
                    We're on a mission to make technology serve humanity again.
                </p>
                <p class="text-3xl md:text-5xl font-medium leading-tight">
                    Sign up to know when we launch.
                </p>
            </div>
            
            <!-- Intake Form -->
            <form class="max-w-2xl">
                <div class="flex flex-col gap-4">
                    <input 
                        name="email"
                        type="email" 
                        placeholder="Enter your email"
                        class="px-6 py-4 text-xl bg-transparent border-2 border-white text-white placeholder-gray-400 focus:outline-none focus:border-gray-300 transition-colors"
                        required
                    >
                    <textarea 
                        name="excitement"
                        placeholder="What's got you excited?"
                        rows="4"
                        class="px-6 py-4 text-xl bg-transparent border-2 border-white text-white placeholder-gray-400 focus:outline-none focus:border-gray-300 transition-colors resize-vertical"
                    ></textarea>
                    <input type="hidden" name="custom-source" value="none">
                    <input type="hidden" name="version" value="a">
                    <button 
                        type="submit"
                        class="px-8 py-4 text-xl bg-white text-black font-medium hover:bg-gray-200 transition-colors"
                    >
                        Join
                    </button>
                </div>
            </form>
        </section>
    """)
    
    return render_base(content, "a") 