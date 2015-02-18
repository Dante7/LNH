# Create your views here.
#encoding:utf-8
from django.db import models
from captura.models import *
from captura.forms import *
from django.shortcuts import render_to_response

def Inicio(request):
	plantilla = 'inicio.html'
	if request.method == 'POST':
		formulario = FrmTbl1(request.post)
		if formulario.is_valid():
			formulario.save()
			return render_to_response(plantilla, {'form':formulario})
	else:
		formulario = FrmTbl1() 
	return render_to_response(plantilla, {'form':formulario})