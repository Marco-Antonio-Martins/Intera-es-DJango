from django.urls import reverse
from app.models import MensagemDeContato
from .forms import ContatoForm, PublicacaoForm
from django.views.generic import FormView, TemplateView



class ContatoView(FormView):
    template_name = 'app/contato.html'
    form_class = ContatoForm 

    def form_valid(self, form):
        dados = form.clean()
        print(dados)
        mensagem = MensagemDeContato(nome=dados['nome'], email=dados['email'], mensagem=dados['mensagem'])
        mensagem.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('contato_sucesso')


class ContatoSucessoView(TemplateView):
    template_name = 'app/contato_sucesso.html'

class PublicacaoView(FormView):
    template_name = 'app/publicacao.html'
    form_class = PublicacaoForm 

'''    def form_valid(self, form):
        dados = form.clean()
        print(dados)
        mensagem = MensagemDeContato(nome=dados['nome'], email=dados['email'], mensagem=dados['mensagem'])
        mensagem.save()
        return super().form_valid(form)'''