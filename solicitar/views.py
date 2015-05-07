from django.shortcuts import render

# Create your views here.
def solicitar(request):
	marcas = Marca.objects.all()
    return render(request, 'solicitar.html' , marcas)