from django.urls import path
from .views import index, portifolio, certificado, filtroPortifolio, ordemPortifolio


urlpatterns = [
    path('', index, name='index'),
    path('portifolio/', portifolio, name='portifolio'),
    path('certificado/', certificado, name='certificado'),
    path('portifolio/filtro/<str:categoria>', filtroPortifolio, name='filtro'),
    path('portifolio/ordem/<str:ordem>', ordemPortifolio, name='ordem'),
]