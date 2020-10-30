from . import views
from django.urls import path

urlpatterns = [
    path("", views.index),
    path("submit_guess", views.submit_guess),
    path("result", views.result)
]
