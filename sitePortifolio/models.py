from django.db import models
from datetime import datetime

OPCOES_TIPO = [
    ('Python','Python'),
    ('Django','Django'),
    ('React','React'),
    ('Golang','Golang'),
    ('JavaScript','JavaScript'),
]
OPCOES_AREA = [
    ('Programação','Programação'),
    ('Front-end','Front-end'),
    ('Ux-designer','Ux-designer'),
    ('Devops','Devops'),
    ('Banco-de-dados','Banco de dados'),
]

class ProjetosBd(models.Model):
    imagem = models.ImageField(upload_to="fotos/", blank=False, null=False)
    titulo = models.CharField(max_length=100, blank=False, null=False)
    tipo = models.CharField(max_length=100, blank=False, null=False, choices=OPCOES_TIPO)
    nota = models.IntegerField(blank=False, null=False)
    data_postagem = models.DateTimeField(default=datetime.now, blank=False)
    linkgit = models.CharField(max_length=100, blank=False, null=False, default='qualquercoisa')
    linksite = models.CharField(max_length=100, blank=False, null=False, default='qualquercoisa')

class CertificadosBd(models.Model):
    foto = models.ImageField(upload_to="fotos_certificado", blank=False, null=False)
    categoria = models.CharField(choices=OPCOES_AREA, blank=False, null=False, max_length=100)