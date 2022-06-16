from django.urls import path

from webapp.views import main_view

urlpatterns = [
    path('', main_view)
    ]