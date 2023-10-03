from django.shortcuts import render
from django.views.generic.base import TemplateView

# Importing modules to create XHR request
from django.http.response import JsonResponse 
from django.views.decorators.csrf import csrf_exempt 
from django.conf import settings

import stripe
# Create your views here.
class HomePayView(TemplateView):
    template_name = 'payHome.html'

# View to notify success
class SuccessView(TemplateView):
    template_name = 'success.html'

# View to notify cancellation
class CancelledView(TemplateView):
    template_name = 'cancelled.html'

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'https://www.smatwebsite.co.uk/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - capture the payment later
            # [customer_email] - prefill the email input in the form
            # For full details see https://stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[{
                        'price_data':{
                            'unit_amount':1000,
                            'product_data':{'name': 'coffee'},
                            'currency': 'gbp',
                                      },
                        'quantity': 1,
                    }]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})