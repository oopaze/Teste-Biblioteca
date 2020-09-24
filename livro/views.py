from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm


def exibir_livros(request):
    livros = Livro.objects.all()
    return render(request, 'livro/index.html', {'livros':livros})

def adicionar_livro(request):
    form = LivroForm(request.POST or None)
    numero_de_autores = len(form.fields['autor'].queryset)

    if form.is_valid():
        form.save()
        return redirect('exibir_livros')

    return render(request, 'livro/adicionar.html', {'form':form, 'numero_de_autores':numero_de_autores})

def atualizar_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)
    form = LivroForm(request.POST or None, request.FILES or None, instance=livro)

    if form.is_valid():
        form.save()
        return redirect('exibir_livros')

    return render(request,'livro/atualizar.html', {'form':form})

def deletar_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)

    if request.method == 'POST':
        livro.delete()
        return redirect('exibir_livros')

    return render(request,'livro/deletar.html', {'livro':livro})
