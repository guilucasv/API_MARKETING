from unicodedata import decimal
from django.db import models


#Models para cadastro das Empresas no Django Admin
class Empresa(models.Model):
    Nome = models.CharField(max_length=50)
    Site = models.URLField(max_length=100)
    Instagram = models.URLField(max_length=100, null=True)
    Responsavel = models.CharField(max_length=50, null=True)
    Telefone_do_Responsavel = models.CharField(max_length=50)

    #Retorna o nome da empresa(.Nome) na apresentação no painel
    def __str__(self):
        return self.Nome

#Models para cadastro dos Anúncios no Django Admin
class Anuncio(models.Model):
    Nome_do_Anuncio = models.CharField(max_length=50)
    Data_Inicial = models.DateField()
    Data_Final = models.DateField()
    Valor_do_Anuncio = models.DecimalField(max_digits=9, decimal_places=2)
    Anexos = models.FileField(upload_to="C:/Users/lucas.silva/Documents/APP_MARKETING/imagens")
    Tempo_do_Anuncio = models.PositiveIntegerField()
    Codigo_da_Empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING, related_name='codigo_da_empresa')

    #Retorna o nome do anúncio(.Nome_do_Anuncio) na apresentação no painel
    def __str__(self):
        return self.Nome_do_Anuncio