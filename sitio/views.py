from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html' )
def nosotros(request):
    return render(request, 'nosotros.html' )
def contactanos(request):
    return render(request, 'contactanos.html' )
def accesorios(request):
    return render(request, 'proximamente.html' )
def base(request):
    return render(request, 'base.html' )