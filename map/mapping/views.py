from django.shortcuts import render

# Create your views here.
def map(request):
    return render(request,"map.html")

def museum(request):
    return render(request,"main.html")

def botanical(request):
    return render(request,"botanical.html")

def bronze(request):
    return render(request,"bronze.html")

def children(request):
    return render(request,"children.html")
    
def theater(request):
    return render(request,"theater.html")
    