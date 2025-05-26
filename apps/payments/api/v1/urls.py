from django.urls import path
from apps.payments.services import (
    CreateCheckoutSessionView,
    stripe_webhook
)
app_name = "payments"

urlpatterns = [
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('webhooks/stripe/', stripe_webhook),
]
