from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('apr/<int:day_id>', views.apr),
    path('may/<int:day_id>', views.may),
    path('jun/<int:day_id>', views.jun),
    path('jul/<int:day_id>', views.jul),
    path('aug/<int:day_id>', views.aug),
    path('sep/<int:day_id>', views.sep),
    path('dsa/<topic>', views.dsa, name='dsa'),
    path('articles/<topic>',views.articles, name='articles'),
]