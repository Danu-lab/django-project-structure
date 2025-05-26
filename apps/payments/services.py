from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

import stripe
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .constants import (
    STRIPE_SECRET_KEY,
    STRIPE_PUBLIC_KEY,
    STRIPE_WEBHOOK_SECRET
)

stripe.api_key = STRIPE_SECRET_KEY

class CreateCheckoutSessionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        domain = 'http://localhost:3000'  # Replace with your frontend
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'Premium Subscription',
                        },
                        'unit_amount': 1000,  # $10.00
                        'recurring': {'interval': 'month'},
                    },
                    'quantity': 1,
                }],
                mode='subscription',
                success_url=domain + '/success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain + '/cancel',
                customer_email=request.user.email,
            )
            return Response({'url': checkout_session.url})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)

    # Handle subscription completed
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print('Payment succeeded for user:', session.get('customer_email'))

    return HttpResponse(status=200)
