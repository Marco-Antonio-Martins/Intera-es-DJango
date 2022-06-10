from unicodedata import name
from django.contrib import admin
from django.urls import path
from app.views import ContatoView, ContatoSucessoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ContatoView.as_view(), name=""),
    path('sucesso', ContatoSucessoView.as_view(), name="contato_sucesso")
]
