from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

def index(request):
    return render(request, 'madlibsApp/home.html')

def profile(request):
    req = requests.get("http://madlibz.herokuapp.com/api/random")
    data = req.json()
    title = data['title']
    return HttpResponse(title)


