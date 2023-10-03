from django.urls import path 
from . import views 

urlpatterns = [
    path('payment/', views.HomePayView.as_view(), name='payHome'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.SuccessView.as_view(), name='successfulPayment'),
    path('cancelled/', views.CancelledView.as_view(), name='cancelledPayment')
]