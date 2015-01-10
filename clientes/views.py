from django.shortcuts import render, render_to_response
from clientes.models import Country
from clientes import SaveDicc
# Create your views here.
def C_Registrar_View(request):
    diccionary = {}
    a = SaveDicc()
    a.get({'id':'dd'})
    diccionary['country'] = Country.objects.all()

    return render_to_response("index.html", diccionary)