from cProfile import label
from unicodedata import lookup
import django_filters
from django_filters import CharFilter, NumberFilter, DateFilter
from .models import *


class FarmersFilter(django_filters.FilterSet):
    first_name = CharFilter(field_name='first_name',
                            lookup_expr='icontains', label='First Name')
    second_name = CharFilter(field_name='second_name',
                             lookup_expr='icontains', label='Second Name')

    class Meta:
        model = Farmer
        fields = ['first_name', 'second_name']




class ProducerFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains', label='Name')
    generic_name = CharFilter(field_name='generic_name', lookup_expr='icontains', label='generic name')

    class Meta:
        model = Produce
        fields = ['name']


        fields = ['name', 'generic_name']



class InvoiceFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_created',
                            lookup_expr='gte', label='Start Date')
    end_date = DateFilter(field_name='date_created',
                          lookup_expr='lte', label='End Date')

    class Meta:
        model = Invoice
        fields = ['customer', 'status', ]
