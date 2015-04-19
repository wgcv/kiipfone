# -*- encoding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from usuario.models import *

class RegistrarUser(UserCreationForm):
	username = forms.CharField(
		max_length=150,
		label = 'Usuario'
	)
	email = forms.CharField(
		max_length=150,
		label = 'E-mail'
	)
	def __init__(self, *args, **kwargs):
		super(RegistrarUser, self).__init__(*args, **kwargs)
		self.fields['password1'].label = 'Contraseña'
		self.fields['password2'].help_text = None
		self.fields['password2'].label = 'Repite contraseña'
	class Meta:
			model = User
			fields = ('username','email')


class RegistrarseUsuario(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = ('celular',)
