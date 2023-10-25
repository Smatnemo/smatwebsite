from django.shortcuts import render
from django.views.generic.base import TemplateView

# Importing modules to create XHR request
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt 
from django.conf import settings

import stripe
# Create your views here.
class HomePayView(TemplateView):
    template_name = 'payments/payHome.html'

# View to notify success
class SuccessView(TemplateView):
    template_name = 'payments/success.html'

# View to notify cancellation
class CancelledView(TemplateView):
    template_name = 'payments/cancelled.html'

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request, product):
    # A list of the available products
    domain_url = 'https://www.smatwebsite.co.uk/'
    stripe.api_key = settings.STRIPE_SECRET_KEY
    success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}'
    cancel_url=domain_url + 'cancelled/'

    # Create new Checkout Session for the order
    # Other optional params include:
    # [billing_address_collection] - to display billing address details on the page
    # [customer] - if you have an existing Stripe Customer ID
    # [payment_intent_data] - capture the payment later
    # [customer_email] - prefill the email input in the form
    # For full details see https://stripe.com/docs/api/checkout/sessions/create

    # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
    if request.method == 'GET' and product == 'coffee':
        
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=success_url,
                cancel_url=cancel_url,
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
            print("I am here:", product)
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    elif request.method == 'GET' and product == 'beer':
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=success_url,
                cancel_url=cancel_url,
                payment_method_types=['card'],
                mode='payment',
                line_items=[{
                        'price_data':{
                            'unit_amount':1500,
                            'product_data':{'name': 'beer'},
                            'currency': 'gbp',
                                      },
                        'quantity': 1,
                    }]
            )
            print("I am here:", product)
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})
        
    elif request.method == 'GET' and product == 'crate':
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=success_url,
                cancel_url=cancel_url,
                payment_method_types=['card'],
                mode='payment',
                line_items=[{
                        'price_data':{
                            'unit_amount':12000,
                            'product_data':{'name': 'crate'},
                            'currency': 'gbp',
                                      },
                        'quantity': 1,
                    }]
            )
            print("I am here:", product)
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    
    else:
        return render(request, 'payment/')

        

@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        print("Payment was successful.")
        # TODO: run some custom code here

    return HttpResponse(status=200)
