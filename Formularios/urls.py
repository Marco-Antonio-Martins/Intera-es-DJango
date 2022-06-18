from django.contrib import admin
from django.urls import path, include
from app.views import ContatoView, ContatoSucessoView, PublicacaoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ContatoView.as_view(), name="contatoView"),
    path('sucesso', ContatoSucessoView.as_view(), name="contato_sucesso"),
    path('conta/', include("django.contrib.auth.urls")),
    path('publicacao/', PublicacaoView.as_view(), name="publicacao")
]
