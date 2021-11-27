#from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def fun(request):
    today=datetime.datetime.now()
    return HttpResponse("Hi cuties Aumber and zane Mommy and Daddy love you both<br/>"+str(today))
