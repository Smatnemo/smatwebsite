from django.urls import path 
from . import views 

urlpatterns = [
    path('payment/', views.HomePayView.as_view(), name='payHome'),
    path('config/', views.stripe_config),
]