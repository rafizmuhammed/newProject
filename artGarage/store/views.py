from django.shortcuts import render,redirect
from .models import categories,collections

# Create your views here.

def index(request):
    return render(request,'index.html')

def category(request):
    obj = categories.objects.all()
    return render(request,'category.html',{'object':obj})

def collection(request):
    p_id = request.GET['id']
    obj = categories.objects.get(id = p_id)
    return render(request,'collections.html',{'obj1':obj})

def product(request):
    p_id = request.GET['id']
    obj = collections.objects.get(id = p_id)
    return render(request,'product.html',{'obj2':obj})