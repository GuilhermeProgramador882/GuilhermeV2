from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Movimentacao, Categoria
from .forms import MovimentacaoForm, CategoriaForm
from .filters import MovimentacaoFilter

@login_required
def lista_movimentacoes(request):
    movimentacoes = Movimentacao.objects.filter(usuario=request.user)

    filtro = MovimentacaoFilter(request.GET, queryset=movimentacoes)
    movimentacoes = filtro.qs

    total_receitas = movimentacoes.filter(categoria__tipo='receita').aggregate(Sum('valor'))['valor__sum'] or 0
    total_despesas = movimentacoes.filter(categoria__tipo='despesa').aggregate(Sum('valor'))['valor__sum'] or 0
    saldo = total_receitas - total_despesas

    return render(request, 'movimentacoes/lista.html', {
        'filtro': filtro,
        'movimentacoes': movimentacoes,
        'total_receitas': total_receitas,
        'total_despesas': total_despesas,
        'saldo': saldo,
    })


@login_required
def criar_movimentacao(request):
    form = MovimentacaoForm(request.POST or None)
    if form.is_valid():
        mov = form.save(commit=False)
        mov.usuario = request.user
        mov.save()
        return redirect('lista_movimentacoes')
    return render(request, 'movimentacoes/form.html', {'form': form})


@login_required
def editar_movimentacao(request, id):
    mov = get_object_or_404(Movimentacao, id=id, usuario=request.user)
    form = MovimentacaoForm(request.POST or None, instance=mov)
    if form.is_valid():
        form.save()
        return redirect('lista_movimentacoes')
    return render(request, 'movimentacoes/form.html', {'form': form})


@login_required
def excluir_movimentacao(request, id):
    mov = get_object_or_404(Movimentacao, id=id, usuario=request.user)
    mov.delete()
    return redirect('lista_movimentacoes')
