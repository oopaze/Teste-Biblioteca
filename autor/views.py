from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Autor
from .forms import AutorForm

def exibir_autor(request):
    autores = Autor.objects.all()

    return render(request, 'autor/index.html', {'autores':autores})

def criar_autor(request):
    form = AutorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('exibir_autor')

    return render(request, 'autor/criar.html', {'form':form})

def atualizar_autor(request, id):
    autor = get_object_or_404(Autor, pk=id)
    form = AutorForm(request.POST or None, request.FILES or None, instance=autor)

    if form.is_valid():
        form.save()
        return redirect('exibir_autor')

    return render(request, 'autor/atualizar.html', {'form':form})


def deletar_autor(request, id):
    autor = get_object_or_404(Autor, pk=id)

    if request.method == 'POST':
        autor.delete()
        return redirect('exibir_autor')

    return render(request, 'autor/deletar.html', {'autor':autor})
