from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.


def say_hello():
    return HttpResponse("Hello welcome to Savvy Store")