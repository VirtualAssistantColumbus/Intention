from components.base import base
from components.nav import nav
from shared_dependencies import route
from utils.html_ import html


@route('/boredom-letter-2-post-sign-up')
def render_boredom_letter_2_post_sign_up() -> str:
    """ Thank you page after form submission. """

    content = html(f"""
        <!-- Question Header -->
        <section class="px-8 pt-16 pb-8 md:px-16 lg:px-24">
            <h1 class="text-massive-mobile md:text-massive font-bold mb-10 leading-none tracking-tight">
                Thank you and quick question
            </h1>

            <div class="max-w-4xl space-y-8">
                <p class="text-xl md:text-2xl leading-relaxed font-bold">
                    What was it about our mission that resonated with you?
                </p>
                
                <p class="text-xl md:text-2xl leading-relaxed">
                    We just <strong>sent you an email</strong> with this question in it.
                    If you have a minute, could you <strong>write us a response</strong> while this is top of mind?
                </p>
                <p class="text-xl md:text-2xl leading-relaxed">
                    We personally read every message, and your thoughts will help inspire what we build.
                </p>
                <p class="text-xl md:text-2xl leading-relaxed">
                    Thank you for joining our mission to make technology serve humanity again.
                </p>
                <p class="text-xl md:text-2xl leading-relaxed">
                    Sincerely,<br>
                    The Intention Team
                </p>
                   
        { nav() }
    """)
    
    return base(content)