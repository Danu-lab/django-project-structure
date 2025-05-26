from django.core.mail import send_mail
from django.conf import settings

def send_verification_email(email, token):
    subject = "Verify your account"
    verification_link = f"http://localhost:8000/api/users/verify/?token={token}"
    message = f"Hi! Click the link to verify your account: {verification_link}"
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
