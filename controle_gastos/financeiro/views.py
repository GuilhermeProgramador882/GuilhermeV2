from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator

# Logout somente via POST
@method_decorator(require_POST, name='dispatch')
class LogoutPostOnlyView(LogoutView):
    # redireciona para a página de login após logout
    next_page = '/login/'

from django.db.models import Sum
from .models import Movimentacao, Categoria
from .forms import MovimentacaoForm, CategoriaForm
from .filters import MovimentacaoFilter

@login_required
def lista_movimentacoes(request):
    movimentacoes = Movimentacao.objects.filter(usuario=request.user).order_by('-data')

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
def dashboard(request):
    """Resumo financeiro: totais e últimas movimentações do usuário"""
    movimentacoes = Movimentacao.objects.filter(usuario=request.user)

    total_receitas = movimentacoes.filter(categoria__tipo='receita').aggregate(Sum('valor'))['valor__sum'] or 0
    total_despesas = movimentacoes.filter(categoria__tipo='despesa').aggregate(Sum('valor'))['valor__sum'] or 0
    saldo = total_receitas - total_despesas

    ultimas = movimentacoes.order_by('-data')[:5]

    return render(request, 'dashboard.html', {
        'total_receitas': total_receitas,
        'total_despesas': total_despesas,
        'saldo': saldo,
        'ultimas': ultimas,
    })


@login_required
def criar_movimentacao(request):
    form = MovimentacaoForm(request.POST or None)
    if form.is_valid():
        mov = form.save(commit=False)
        mov.usuario = request.user
        mov.save()
        return redirect('lista_movimentacoes')
    return render(request, 'movimentacoes/form.html', {'form': form, 'titulo': 'Nova Movimentação'})


@login_required
def editar_movimentacao(request, id):
    mov = get_object_or_404(Movimentacao, id=id, usuario=request.user)
    form = MovimentacaoForm(request.POST or None, instance=mov)
    if form.is_valid():
        form.save()
        return redirect('lista_movimentacoes')
    return render(request, 'movimentacoes/form.html', {'form': form, 'titulo': 'Editar Movimentação'})


@login_required
def excluir_movimentacao(request, id):
    mov = get_object_or_404(Movimentacao, id=id, usuario=request.user)
    if request.method == 'POST':
        mov.delete()
        return redirect('lista_movimentacoes')
    return render(request, 'movimentacoes/confirmar_excluir.html', {'movimentacao': mov})


@login_required
def lista_categorias(request):
    categorias = Categoria.objects.filter(usuario=request.user).order_by('nome')
    return render(request, 'categorias/lista.html', {'categorias': categorias})


@login_required
def criar_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        cat = form.save(commit=False)
        cat.usuario = request.user
        cat.save()
        return redirect('lista_categorias')
    return render(request, 'categorias/form.html', {'form': form, 'titulo': 'Nova Categoria'})


@login_required
def editar_categoria(request, id):
    cat = get_object_or_404(Categoria, id=id, usuario=request.user)
    form = CategoriaForm(request.POST or None, instance=cat)
    if form.is_valid():
        form.save()
        return redirect('lista_categorias')
    return render(request, 'categorias/form.html', {'form': form, 'titulo': 'Editar Categoria'})


@login_required
def excluir_categoria(request, id):
    cat = get_object_or_404(Categoria, id=id, usuario=request.user)
    if request.method == 'POST':
        cat.delete()
        return redirect('lista_categorias')
    return render(request, 'categorias/confirmar_excluir.html', {'categoria': cat})

