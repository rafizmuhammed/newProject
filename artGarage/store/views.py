from django.shortcuts import render,redirect
from .models import categories

# Create your views here.

def index(request):
    return render(request,'index.html')

def category(request):
    obj = categories.objects.all()
    return render(request,'category.html',{'object':obj})