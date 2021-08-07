from swati.models import Destination
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'swati'})

def add(request):
    val1 = request.POST["num1"]
    val2 = request.POST["num2"]
    # val2 = request.GET["num2"]
    res = int(val1)+int(val2)
    return render(request,'result.html',{'results':res})

def index(request):

    dest = Destination.objects.all()

    return render(request,"index.html",{"dest":dest})