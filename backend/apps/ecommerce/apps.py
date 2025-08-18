from django.apps import AppConfig


class EcommerceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.ecommerce'
    label = 'ecommerce'
    verbose_name = 'E-commerce'