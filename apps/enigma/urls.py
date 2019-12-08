from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^enigma-pricing', views.pricing),
    url(r'^buy-enigma-platinum', views.platinum)
]