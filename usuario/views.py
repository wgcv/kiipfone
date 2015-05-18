from django.shortcuts import render
from usuario.forms import RegistrarUser,RegistrarseUsuario
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login

# Create your views here.
def registro(request):
	if request.method == 'POST':
		user = RegistrarUser(request.POST)
		usuario = RegistrarseUsuario(request.POST)
		if user.is_valid() and usuario.is_valid():
			user.save()
			useradd = User.objects.get(username=user.cleaned_data['username'])
			usuario = usuario.save(commit=False)
			usuario.user = useradd
			usuario.save()
			user = authenticate(username=request.POST['username'], password=request.POST['password1'])
			login(request, user)

		return HttpResponseRedirect(request.GET['next'])
			
	else:
		return render(request, 'registrarse.html', dict(RegistrarUser=RegistrarUser(), RegistrarseUsuario=RegistrarseUsuario()))