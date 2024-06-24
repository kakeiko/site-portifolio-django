import django_filters
from .models import CertificadosBd

class FiltroCertificado(django_filters.FilterSet):
    class Meta:
        model = CertificadosBd
        fields = {
            "categoria": ["exact"],
        }