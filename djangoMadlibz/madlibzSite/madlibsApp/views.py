from django.shortcuts import render
import requests
from django.http import HttpResponse
import json
from django.http import QueryDict



req = requests.get("http://madlibz.herokuapp.com/api/random")
data = req.json()


def index(request):
    return render(request, 'madlibsApp/home.html')


def profile(request):
    if request.method == "POST":
        newDict2 = request.POST
        newDict = dict(newDict2._iterlists())
        pleaseWork = zip(data['value'], newDict['user'])
        return render(request, "madlibsApp/answers.html",
                      {'newDict': newDict, 'data': data, 'pleaseWork': pleaseWork}, )
    return render(request, "madlibsApp/home.html", {'data': data})


def answers(request):
    if request.method == 'POST':
        newDict2 = request.POST
        newDict = dict(newDict2._iterlists())
        pleaseWork = zip(data['value'], newDict['user'])
    return render(request, "madlibsApp/answers.html",
                {'newDict': newDict, 'data': data, 'pleaseWork': pleaseWork}, )

def again(request):
    req = requests.get("http://madlibz.herokuapp.com/api/random")
    data = req.json()
    # if request.method == "POST":
    #     newDict2 = request.POST
    #     newDict = dict(newDict2._iterlists())
    #     pleaseWork = zip(data['value'], newDict['user'])
    #     return render(request, "madlibsApp/answers.html",
    #                   {'newDict': newDict, 'data': data, 'pleaseWork': pleaseWork}, )
    return render(request, "madlibsApp/home.html", {'data': data})
