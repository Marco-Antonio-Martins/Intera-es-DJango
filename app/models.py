from django.db import models

class MensagemDeContato(models.Model):
    class Meta:
        verbose_name = 'Mensagem de contato'
        verbose_name_plural = 'Mensagens de contato'

    
    nome = models.CharField(max_length=128)
    email = models.EmailField('E-mail', null=True, blank=True)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True, null=True)