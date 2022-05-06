from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('', views.BlankView.as_view(), name='main'),
    #path('update/<int:pk>', views.BlankUpdateView.as_view(), name='update'),
]
