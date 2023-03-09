from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def Vamsi(request):
    return HttpResponse('<h1>Vamsi likes playing cricket<h1/>S')
