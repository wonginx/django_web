from django.urls import path

from openapp.views import open_world

urlpatterns = [


    path('open_world/', open_world, name='open_world'),
    ]