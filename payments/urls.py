from django.urls import path 
from . import views 

urlpatterns = [
    path('payment/', views.HomePayView.as_view(), name='payHome'),
    path('config/', views.stripe_config),
    path('create-checkout-session/<product>', views.create_checkout_session),
    path('success/', views.SuccessView.as_view(), name='successfulPayment'),
    path('cancelled/', views.CancelledView.as_view(), name='cancelledPayment'),
    path('webhook/', views.stripe_webhook),
]