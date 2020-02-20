from django.urls import path

from demo.main import views

urlpatterns = [
    path('home', views.index)
]
