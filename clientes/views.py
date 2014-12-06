from django.shortcuts import render, render_to_response
from clientes.models import Country

# Create your views here.
def C_Registrar_View(request):
	diccionary = {}
	diccionary['country'] = Country.objects.all()

	return render_to_response("index.html", diccionary)