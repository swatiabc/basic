from django import forms
from swati.forms import DestinationForm
from swati.models import Destination
from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.

def home(request):
    form = DestinationForm(request.POST or None, request.FILES or None )
    if form.is_valid():
        form.save()
    return render(request,'home.html',{"form":form})

def add(request):
    
    return render(request,'result.html')

def index(request):

    dest = Destination.objects.all()

    return render(request,"index.html",{"dest":dest})

def edit(request,id):
    dest = Destination.objects.get(id=id)
    return render(request,"edit.html",{"dest":dest})

def update(request,id):
    dest = Destination.objects.get(id=id)
    form = DestinationForm(request.POST or None, instance=dest )
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request,"edit.html",{"dest":dest})

def remove(request,id):
    dest = Destination.objects.get(id=id)
    dest.delete()
    return redirect("index")