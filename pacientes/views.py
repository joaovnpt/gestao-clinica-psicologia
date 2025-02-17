from django.shortcuts import render, HttpResponse
from .models import Pacientes

def pacientes(request):
    queixas = Pacientes.queixa_choices
    if request.method == 'GET':
        return render(request, 'pacientes.html', {'queixas': queixas})
    elif request.method == 'POST':
        print(request.POST)
        return HttpResponse('aa')