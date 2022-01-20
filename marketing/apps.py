from django.apps import AppConfig

#Criação do app que foi definido em "settings" da pasta 'CONFIG'
class MarketingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'marketing'
