from django.contrib import admin
from marketing.models import Empresa
from marketing.models import Anuncio


#Definir a informação da empresa que irá aparecer no painel de administração.
class Empresas(admin.ModelAdmin):
    list_display = ('id', 'Nome', 'Site', 'Instagram', 'Responsavel', 'Telefone_do_Responsavel')
    list_display_links = ('Nome', 'Site', 'Instagram', 'Responsavel', 'Telefone_do_Responsavel')
    search_fields = ('Nome',)

#Definir a informação do anúncio que irá aparecer no painel de administração.
class Anuncios(admin.ModelAdmin):
    list_display = ('id', 'Nome_do_Anuncio', 'Data_Inicial', 'Data_Final', 'Valor_do_Anuncio', 'Anexos', 'Tempo_do_Anuncio', 'Codigo_da_Empresa') 
    list_display_links = ('Nome_do_Anuncio', 'Data_Inicial', 'Data_Final', 'Valor_do_Anuncio', 'Anexos', 'Tempo_do_Anuncio',)
    search_fields = ('Nome_do_Anuncio',)
    list_filter = ('Nome_do_Anuncio',)


admin.site.register(Empresa, Empresas)
admin.site.register(Anuncio, Anuncios)