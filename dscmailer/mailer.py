from decouple import config
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_mail(sender,receiver,subject,html, api_key):
    """
    Use this function to set up the `email sender`, `the recipient`, `email subject`,  the `html content` of the email and the `api_key` from Sendgrid..

    """
    message = Mail(
        from_email=sender,
        to_emails=receiver,
        subject=subject,
        html_content=html
        )

    try:
        API_KEY = api_key
        sg = SendGridAPIClient(API_KEY)
        response = sg.send(message)
        print('Email sent successfully.')
    except Exception as e:
        print(f'Error while sending email. {e}')    