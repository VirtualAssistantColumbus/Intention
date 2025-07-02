from request_context import get_context
from utils.html_ import html
from components.render_base import render_base
from shared_dependencies import route


@route('/enddoomscrolling-letter')
def render_enddoomscrolling_letter() -> str:
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
                    "Why am I looking at a flyer with nothing on it but enddoomscrolling.com?"
                </p>
                
                <p class="text-xl md:text-2xl leading-relaxed">
                    Well, because that's the mission of our company, Intention. We are a Columbus-based startup on a mission to end doomscrolling and improve the relationship between humanity and the technology we use on a daily basis.
                </p>
                
                <p class="text-xl md:text-2xl leading-relaxed">
                    The average person will spend about 9 years of their life chasing down social media rabbit holes. We don't know about you, but we think that's unacceptable.
                </p>
                
                <p class="text-xl md:text-2xl leading-relaxed">
                    You see, it's not just the scrolling itself that bothers us, it's what the scrolling replaces that's most concerning.
                </p>
                
                <p class="text-xl md:text-2xl leading-relaxed">
                    Meaningful connection. Peace of mind. Moments of reflection. Downtime. Time to process your thoughts and emotions.
                </p>
                
                <p class="text-xl md:text-2xl leading-relaxed">
                    Heck, boredom even.
                </p>
                
                <p class="text-xl md:text-2xl leading-relaxed">
                    We believe that these are essential functions for human beings to thrive, and yet they've gone noticeably missing from our modern-day society.
                </p>
                
                <p class="text-xl md:text-2xl leading-relaxed">
                    That's why we've made it our mission to fix our relationship with technology.
                </p>
                
                <p class="text-xl md:text-2xl leading-relaxed">
                    We believe that technology should serve humanity, not take advantage of us. Technology should help each of us rise to our highest selves, instead of keeping us trapped in our worst habits. Technology should empower us rather than drain us.
                </p>
                
                <p class="text-xl md:text-2xl leading-relaxed">
                    Today we are far from that vision. Every day, we are bombarded by an endless stream of notifications and messages. We consume social media feeds that never end, designed to be as addictive as possible. We deal with so much information that most of us feel completely overwhelmed.
                </p>
                
                <p class="text-xl md:text-2xl leading-relaxed">
                    At Intention, we think we all deserve better.
                </p>
                
                <p class="text-xl md:text-2xl leading-relaxed">
                    We believe that every app you use should respect your attention as if it were the most valuable asset you have—because it is.
                </p>
                
                <p class="text-xl md:text-2xl leading-relaxed">
                    We believe that you should control your devices, instead of your devices controlling you. That you should be able to access the apps you need, without a million distractions trying to make you forget why you opened the app in the first place.
                </p>
                
                <p class="text-xl md:text-2xl leading-relaxed">
                    So that's what we're building.
                </p>           

                <p class="text-xl md:text-2xl leading-relaxed">
                    We're reimagining the apps and devices you use on a daily basis to give you control of what you want to see, and what you don't.
                </p>
                
                <p class="text-xl md:text-2xl leading-relaxed">
                    We're designing a paradigm shift in the way you connect with social media and your devices, by creating apps that begin and end with intention.
                </p>
                
                <p class="text-xl md:text-2xl leading-relaxed">
                    We're tackling the problem head on, and we need your support to make it happen.
                </p>
            </div>

            <div class="max-w-4xl space-y-8 mb-12 mt-16">
                <h2 class="text-4xl md:text-5xl font-bold mb-6 leading-tight tracking-tight">
                    Join Us
                </h2>
                <p class="text-xl md:text-2xl leading-relaxed">
                    We're a group of tech veterans who left their jobs to build something meaningful.
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
                            What social media platform should we tackle first? (optional)
                        </p>
                        <textarea 
                            name="comments"
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
    
    return render_base(content)