from django.shortcuts import render
from django.views.generic.base import TemplateView

# Importing modules to create XHR request
from django.http.response import JsonResponse 
from django.views.decorators.csrf import csrf_exempt 
from django.conf import settings

# Create your views here.
class HomePayView(TemplateView):
    template_name = 'payHome.html'

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)
    

