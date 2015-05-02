from django.shortcuts import render

# Create your views here.
def solicitar(request):
    return render(request, 'solicitar.html' )