"""
Webhook endpoints for receiving email signup notifications from Kickoff Labs.

Setup Instructions:
1. In your Kickoff Labs campaign settings, go to "Other Settings" > "API Access"
2. Add your webhook URL (e.g., https://yourdomain.com/webhook/kickoff-labs/signup)
3. Test the webhook using their testing tools
"""

from flask import request, make_response, jsonify
from typing import Dict, Any

from email_marketing.post_sign_up_email import post_sign_up_email
from email_notifications.email_notification_service import EmailNotificationService
from fullstack.frontend.framework.route import Method, app_route
from shared_dependencies import shared

# api.schedulefor.us
@app_route(host=shared.environment.api_host, rule="/webhook/kickoff-labs/signup", methods=[Method.POST])
def kickoff_labs_signup_webhook():
    """
    Webhook endpoint for Kickoff Labs email signup notifications.
    
    Kickoff Labs will POST to this endpoint whenever someone signs up for your campaign.
    The request body contains lead information like email, custom fields, etc.
    """
    try:
        # Parse the incoming webhook data
        webhook_data = _parse_webhook_request()
        
        # Log the webhook for debugging
        shared.logger.info(f"Received Kickoff Labs webhook: {webhook_data}")
        
        # Extract key information
        email = webhook_data.get('email')
        if not email:
            return make_response("Missing email field", 400)
        
        # Process the signup
        _process_email_signup(webhook_data)
        
        # Return success response (Kickoff Labs expects 200 OK)
        return make_response("Webhook processed successfully", 200)
        
    except Exception as e:
        # Log the error
        shared.logger.error(f"Error processing Kickoff Labs webhook: {str(e)}")
        
        # Return error response
        return make_response(f"Webhook processing failed: {str(e)}", 500)


def _parse_webhook_request() -> Dict[str, Any]:
    """
    Parse the incoming webhook request from Kickoff Labs.
    
    Kickoff Labs can send data as either:
    - Form data (application/x-www-form-urlencoded)
    - JSON data (application/json)
    """
    content_type = request.content_type or ""
    
    if "application/json" in content_type:
        # Handle JSON payload
        return request.get_json() or {}
    else:
        # Handle form data (most common for webhooks)
        return dict(request.form)

def _process_email_signup(webhook_data: Dict[str, Any]) -> None:
    """
    Process the email signup from Kickoff Labs.
    
    Common fields from Kickoff Labs:
    - email: The email address
    - given_name: First name
    - family_name: Last name
    - social_id: Unique ID for tracking referrals
    - referrals: Number of referrals this person has
    - custom_fields: Any custom data you collected
    - contest_score: Points earned in the contest
    - ip: IP address of the signup
    """
    
    email = webhook_data.get('email')
    first_name = webhook_data.get('given_name', '')
    last_name = webhook_data.get('family_name', '')
    social_id = webhook_data.get('social_id', '')
    referrals = webhook_data.get('referrals', 0)
    custom_fields = webhook_data.get('custom_fields', {})
    
    # Validate required fields
    if not email:
        raise ValueError("Email is required")
    
    # TODO: Implement your email processing logic here
    # For example:
    # 1. Add to your email marketing list
    # 2. Send welcome email
    # 3. Track signup in analytics
    # 4. Store in database
    # 5. Trigger other workflows
    
    shared.logger.info(f"Processing signup for {email} (ID: {social_id})")
    
    # Initialize email notification service
    shared.logger.debug("Initializing email notification service")
    email_notification_service = EmailNotificationService()
    
    # Generate post-signup email
    shared.logger.info(f"Generating post-signup email for {email}")
    email_to_send = post_sign_up_email(to_email=email)
    
    # Send the email
    shared.logger.info(f"Sending post-signup email to {email}")
    email_notification_service.send(email_to_send)
    shared.logger.info(f"Successfully sent post-signup email to {email}")