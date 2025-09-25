from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def place1(request):
    return render(request, 'main/place1.html')

def place2(request):
    return render(request, 'main/place2.html')


def place3(request):
    return render(request, 'main/place3.html')


def place4(request):
    return render(request, 'main/place4.html')

