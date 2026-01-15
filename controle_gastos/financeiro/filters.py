import django_filters
from .models import Movimentacao

class MovimentacaoFilter(django_filters.FilterSet):
    data = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Movimentacao
        fields = ['descricao', 'categoria', 'valor', 'data']
