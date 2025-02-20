from django.shortcuts import render, redirect
from .models import Pacientes
from django.contrib import messages
from django.contrib.messages import constants

def pacientes(request):
    queixas = Pacientes.queixa_choices
    if request.method == 'GET':
        return render(request, 'pacientes.html', {'queixas': queixas})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        queixa = request.POST.get('queixa')
        foto = request.FILES.get('foto')

        if len(nome.strip()) == 0 or not foto or len(email.strip()) == 0 or len(telefone.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos corretamente.')
            return redirect('pacientes')

    
    pacientes = Pacientes(
        nome=nome,
        email=email,
        telefone=telefone,
        queixa=queixa,
        foto=foto
    )
    pacientes.save()

    messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso')
    return redirect('pacientes')