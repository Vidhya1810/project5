from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def srinu(request):
    return HttpResponse('<h1>srinu is a good boy<h1/>')
