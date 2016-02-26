from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from django.http import QueryDict


# from .forms import answers


req = requests.get("http://madlibz.herokuapp.com/api/random")
data = req.json()

def index(request):
    return render(request, 'madlibsApp/home.html')


def profile(request):
    global data
    if request.method == "POST":
        # req = requests.get("http://madlibz.herokuapp.com/api/random")
        # data = req.json()
        newDict2 = request.POST
        newDict = dict(newDict2._iterlists())
        pleaseWork = zip(data['value'], newDict['user'])
        # for char in ')("':
        #     pleaseWork = pleaseWork2.replace(char, '')
        print(pleaseWork)
        for (a, b) in zip(data['value'], newDict['user']):
            print (a)
            print (b)
        return render(request, "madlibsApp/answers.html",
                      {'newDict': newDict, 'data': data, 'pleaseWork': pleaseWork}, )
    # req = requests.get("http://madlibz.herokuapp.com/api/random")
    # data = req.json()
    return render(request, "madlibsApp/home.html", {'data': data})


def answers(request):
    if request.method == 'POST':
        newDict2 = request.POST
        newDict = dict(newDict2._iterlists())
        pleaseWork = zip(data['value'], newDict['user'])
        for (a, b) in zip(data['value'], newDict['user']):
            print (a)
            print (b)
    return render(request, "madlibsApp/answers.html",
                {'newDict': newDict, 'data': data, 'pleaseWork': pleaseWork}, )


