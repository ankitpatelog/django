from . models import Employee
import django_filters 

class EmployeeFilter(django_filters.filterset):
    designation = django_filters.CharFilter(field_name='designation',lookup_expr='iexact')
    emp_name = django_filters.CharFilter(field_name='emp_name',lookup_expr='icontains')
    # id = django_filters.RangeFilter(field_name='id')
    # this will not work when the id in he format of emp001 to emp010
    # then we need  the charfield with the manual fitlering on it
    id_min = django_filters.CharFilter(method='filter_buy_id_range' , label='From emp to')
    id_max = django_filters.CharFilter(method='filter_buy_id_range' , label='to emp to')
    
    class Meta:
        model = Employee
        fields = ['designation', 'emp_name']
        
    # now filter according to the range 
    
    def filter_buy_id_range(self,queryset,name,value):
        if name == 'id_min':
            return queryset.filter(emp_id__gte=value)
        elif name == 'id_max':
            return queryset.filter(emp_id__lte=value)
        return queryset
            
    
    
    