from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def diwali(request):
    return HttpResponse('Happy Diwali')

def diwali(request):
    return render(request,'diwali.html')
def Newyear(request):
    return render(request,'Newyear.html')