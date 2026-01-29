import django_filters
from .models import Movimentacao, Categoria

class MovimentacaoFilter(django_filters.FilterSet):
    descricao = django_filters.CharFilter(lookup_expr='icontains', label='Descrição')
    categoria = django_filters.ModelChoiceFilter(queryset=Categoria.objects.all())
    valor = django_filters.RangeFilter(label='Valor (entre)')
    data = django_filters.DateFromToRangeFilter(label='Data (período)')

    class Meta:
        model = Movimentacao
        fields = ['descricao', 'categoria', 'valor', 'data']
