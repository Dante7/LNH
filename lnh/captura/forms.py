from django.forms import ModelForm
from django import forms
from captura.models import *

class FrmTbl1(ModelForm):
	class Meta:
		model = Tbl1Hemato
