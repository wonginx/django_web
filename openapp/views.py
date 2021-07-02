from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def open_world(request):
    return HttpResponse('Open world!')