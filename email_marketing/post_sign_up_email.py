from email_notifications.email_notification_service import NewNotificationEmail
from utils.language.dedent import dedent
from fullstack.frontend.utilities.html import Html
from shared_dependencies import shared


def post_sign_up_email(to_email: str) -> NewNotificationEmail:
    """Generates a welcome email for new users after sign up."""
    # Generate the HTML content - Gmail-style minimal
    html_content = Html(dedent(f"""
        <div>
            <p>Hey,</p>
            
            <p>It's Ray, founder of Intention.</p>
            
            <p>I wanted to thank you for believing in us and joining our mission to make technology serve humanity again.</p>
            
            <p>If you have a minute, I'd love to get your thoughts on a quick question:</p>
            <p><strong>What was it about our mission that resonated with you and made you want to sign up?</strong></p>
            
            <p>We're collecting stories, thoughts, and ideas from everyday people about their relationship with technology, social media, and their devices.</p>
                               
            <p>We personally read every single reply, and your response will help inform our design ethos and give us extra motivation to bring this to life.</p>
            
            <p>Thanks!</p>
            <p style="margin-top:32px;">
                <strong>Ray</strong> | Founder<br>
                Intention (<a href="https://www.getintention.io" style="color: #3b82f6; text-decoration: none;">www.getintention.io</a>)<br>
                <span style="color: #6b7280;">Making technology serve humanity again</span>
            </p>
        </div>
    """))
    
    # Generate plain text version
    plain_text = dedent(f"""
        Hey,
        
        It's Ray, founder of Intention.
        
        I wanted to thank you for believing in us and joining our mission.
        
        We want to remake technology to work for everyday people, like you and me, so that we can take our lives back from our devices.
        
        Could you reply back with a response to this question:
        What's social media platform do you want us to fix first? Why?
        
        We personally read every single reply. By replying to this email you'll help us with two things:
        1) Inform our roadmap for app development
        2) Let your email client know that you care about our emails and you don't want them to be filtered into spam.
        
        We'd really appreciate it.
        
        Looking forward to hearing from you!
    """)

    return NewNotificationEmail(
        from_email_address="hello@intentionapps.com",
        from_name="Ray from Intention",
        to_emails=[to_email],
        subject="Thank you and quick question",
        html_content=html_content,
        plain_text_context=plain_text
    )