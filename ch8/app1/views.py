from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1(req):
    return HttpResponse('<h1>app1 content</h1>')