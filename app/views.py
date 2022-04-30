from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.
def insert_data(request):
    FO=TopicForms()
    d={'FO':FO}
    if request.method=='POST':
        FD=TopicForms(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('insterted topic successfully')
    return render(request,'insert_data.html',d)
def webpage_data(request):
    FO=WebpageForms()
    d={'FO':FO}
    if request.method=='POST':
        FD=WebpageForms(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('insteted webpage_data sucessfully ')
    return render(request,'webpage_data.html',d)
