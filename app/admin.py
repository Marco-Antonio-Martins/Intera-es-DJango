from django.contrib import admin
from .models import MensagemDeContato

@admin.register(MensagemDeContato)
class MensagemDeContatoAdmin(admin.ModelAdmin):
    readonly_fields = ('data',)
    