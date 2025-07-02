from utils.html_ import html
from components.base import base
from shared_dependencies import route

@route('/boredom-letter')
def render_boredom_letter() -> str:
    from request_context import get_context
    context = get_context()
    
    content = html(f"""
        <!-- Form Submission Tracking Script -->
        <script>
            document.addEventListener('DOMContentLoaded', function() {{
                const form = document.querySelector('form');
                if (form) {{
                    form.addEventListener('submit', function(e) {{
                        // Track form submission with gtag
                        if (typeof gtag !== 'undefined') {{
                            gtag('event', 'form_submit', {{
                                'event_category': 'engagement',
                                'event_label': 'join_waitlist'
                            }});
                        }}
                        
                        // Track Complete Registration with Facebook Pixel
                        if (typeof fbq !== 'undefined') {{
                            fbq('track', 'CompleteRegistration');
                        }}
                    }});
                }}
            }});
        </script>

        <!-- Open Letter Header -->
        <section class="px-8 pt-16 pb-8 md:px-16 lg:px-24">
            <h1 class="text-massive-mobile md:text-massive font-bold mb-10 leading-none tracking-tight">
                Hi,
            </h1>

            <!-- Letter Content -->
            <div class="max-w-4xl space-y-8">
                <p class="text-xl md:text-2xl leading-relaxed">
                    You're probably wondering.
                </p>
                
                <p class="text-xl md:text-2xl leading-relaxed">
                    "Why are you advertising boredom? Who wants to be bored?"
                </p>
                
                <p class="text-xl md:text-2xl leading-relaxed">
                    That's a great question. And the answer is, well, no one.
                </p>
                
                <p class="text-xl md:text-2xl leading-relaxed">
                    Boredom isn't comfortable. It's a natural instinct that says "hey, maybe you should be doing something instead of just sitting there." Boredom drives us to be curious, to learn new things, and to get out into the world and do things.
                </p>
                
                <p class="text-xl md:text-2xl leading-relaxed">
                    But we think there is another, often ignored, aspect to being bored. Boredom gives you time for your mind to wander, time for your brain to process your thoughts, experiences, and emotions, and time for you to self-reflect and introspect.
                </p>
                
                <p class="text-xl md:text-2xl leading-relaxed">
                    In the modern world, boredom has all but disappeared. Instead, it's been replaced by a never-ending stream of notifications, messages, and social media feeds that are designed to be as addictive as possible. The modern world promises (and delivers) on one thing: you will never have to be bored again.
                </p>
                
                <p class="text-xl md:text-2xl leading-relaxed">
                    In fact, you will never have to really think again either. You will never need to be alone with your thoughts. Never need to confront the things that are bothering you. Never need to deeply consider what you value in life and the type of person you want to be.
                </p>
                
                <p class="text-xl md:text-2xl leading-relaxed">
                    If you're being honest with yourself, how often do you find yourself scrolling endlessly on social media because you're actually avoiding a feeling or a thought? Do you really want to live like you're afraid of your own mind?
                </p>
                
                <p class="text-xl md:text-2xl leading-relaxed">
                    At Intention, we don't think that's an acceptable way to live your life.
                </p>
                
                <p class="text-xl md:text-2xl leading-relaxed">
                    We think what the modern world needs most is more quiet moments of reflection, more self-honesty, and more living with intention instead of distraction.
                </p>
                
                <p class="text-xl md:text-2xl leading-relaxed">
                    That's why we've made it our mission to bring back boredom into the modern world. We're doing this by creating a series of apps that reimagine our relationship with technology. Apps that help you reclaim your attention from addictive devices, and create space for you to have moments of reflection, and maybe even, a little room to breathe.
                </p>
                
                <p class="text-xl md:text-2xl leading-relaxed">
                    Imagine social media feeds with curated content that <strong>ends</strong>, instead of being infinite.
                </p>           

                <p class="text-xl md:text-2xl leading-relaxed">
                    Imagine apps that let you get in and get out, without distractions, so you can do exactly what you intended to do and nothing more.
                </p>
                
                <p class="text-xl md:text-2xl leading-relaxed">
                    Imagine apps designed to help you take control of your devices again, so they don't control you.
                </p>
                
                <p class="text-xl md:text-2xl leading-relaxed">
                    We dream of a world where the apps you use on a daily basis respect your attention as if it were the most valuable asset you have.
                </p>
                
                <p class="text-xl md:text-2xl leading-relaxed">
                    Dream with us.
                </p>
            </div>

            <div class="max-w-4xl space-y-8 mb-12 mt-16">
                <h2 class="text-4xl md:text-5xl font-bold mb-6 leading-tight tracking-tight">
                    Join Us
                </h2>
                <p class="text-xl md:text-2xl leading-relaxed">
                    We're a group of tech veterans who left their jobs to build something meaningful.
                </p>
                <p class="text-xl md:text-2xl leading-relaxed">
                    Over the next few months, we'll be releasing a series of apps designed to reimagine our relationship with our devices. 
                </p>
                <p class="text-xl md:text-2xl leading-relaxed">
                   
                   Sign up to help shape our vision, hear about important updates, and get early access. 
                </p>
                <p class="text-xl md:text-2xl leading-relaxed">
                    No spam.
                </p>           
            </div>
            
            <!-- Conversational Form -->
            <div class="max-w-4xl">
                <form class="space-y-8">
                    <div class="flex flex-col gap-4">
                        <p class="text-xl md:text-2xl leading-relaxed font-bold">
                            How can we reach you?
                        </p>
                        <input 
                            name="email"
                            type="email" 
                            placeholder="your.email@example.com"
                            class="text-xl bg-transparent border-0 border-b-2 border-white text-white placeholder-gray-400 focus:outline-none focus:border-gray-300 transition-colors pb-2"
                            required
                        >
                    </div>
                    <div class="flex flex-col gap-4">
                        <p class="text-xl md:text-2xl leading-relaxed font-bold">
                            Tell us why this message resonates with you (optional).
                        </p>
                        <textarea 
                            name="boredom-resonance"
                            placeholder="Leave any comments or suggestions here!"
                            rows="4"
                            class="text-lg bg-transparent border-2 border-white text-white placeholder-gray-400 focus:outline-none focus:border-gray-300 transition-colors p-4 resize-vertical"
                        ></textarea>
                    </div>
                    <div class="flex flex-col gap-4">
                        <p class="text-xl md:text-2xl leading-relaxed font-bold">
                            Can we reach out to you for feedback on our products? (optional)
                        </p>
                        <div class="flex flex-col gap-3">
                            <label class="flex items-center gap-3 cursor-pointer">
                                <input 
                                    type="radio" 
                                    name="feedback_consent" 
                                    value="yes"
                                    class="w-5 h-5 text-white border-2 border-white bg-transparent focus:ring-white focus:ring-2"
                                >
                                <span class="text-lg md:text-xl">Yes, please reach out</span>
                            </label>
                            <label class="flex items-center gap-3 cursor-pointer">
                                <input 
                                    type="radio" 
                                    name="feedback_consent" 
                                    value="no"
                                    class="w-5 h-5 text-white border-2 border-white bg-transparent focus:ring-white focus:ring-2"
                                >
                                <span class="text-lg md:text-xl">No, just keep me updated</span>
                            </label>
                        </div>
                    </div>
                    <input type="hidden" name="utm_source" value="{context.utm_source or 'none'}">
                    <input type="hidden" name="version" value="{context.version}">
                    <div class="pt-4">
                        <button 
                            type="submit"
                            class="px-8 py-4 text-xl bg-white text-black font-medium hover:bg-gray-200 transition-colors rounded-none"
                        >
                            Count me in
                        </button>
                    </div>
                </form>
            </div>
        </section>
    """)
    
    return base(content)