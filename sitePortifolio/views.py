from django.shortcuts import render
from .models import ProjetosBd, CertificadosBd
from .filters import FiltroCertificado

def index(request):
    return render(request, 'index.html')

def portifolio(request):
    projeto = ProjetosBd.objects.all()
    return render(request, 'portifolio.html', {'cards': projeto})

def certificado(request):
    
    certificado = CertificadosBd.objects.all()
    filtro = FiltroCertificado(request.GET, certificado)
    print(filtro.form.as_p)
    return render(request, 'certificado.html', {'cards': filtro.qs, 'filtro': filtro})

def filtroPortifolio(request, categoria):
    projeto = ProjetosBd.objects.filter(tipo = categoria)
    return render(request, 'portifolio.html', {'cards': projeto})

def ordemPortifolio(request, ordem):
    projeto = ProjetosBd.objects.order_by(ordem)
    return render(request, 'portifolio.html', {'cards': projeto})