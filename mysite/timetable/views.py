from django.shortcuts import render
from django.http import HttpResponse
from .models import Subject

# Create your views here.
def index(request):
    return HttpResponse("This is an example view!")
