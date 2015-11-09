from django.contrib import admin

from .models import Cliente, Funcionario, Historico, Servico
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['nome', 'sobrenome','telefone', 'email', 'data_cadastro']}),
    ]
    list_display = ('ident','nome', 'sobrenome','telefone', 'email', 'data_cadastro')
    list_filter = ['nome','sobrenome']
    search_fields = ['nome','sobrenome']


class FuncionarioAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['nome', 'sobrenome','telefone', 'email', 'data_admissao', 'data_demissao']}),
    ]
    list_display = ('ident','nome', 'sobrenome','telefone', 'email', 'data_admissao', 'data_demissao')
    list_filter = ['nome','sobrenome']
    search_fields = ['nome','sobrenome']


class ServicoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['nome', 'descricao','valor',]}),
    ]
    list_display = ('ident','nome', 'descricao', 'valor')
    list_filter = ['nome']
    search_fields = ['nome']

class HistoricoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Historico',               {'fields': ['cliente', 'funcionario','servicos','data_chamado','data_realizacao']}),
        ('Informacoes', {'fields': ['observacao'], 'classes': ['collapse']}),
    ]
    # inlines = [ServicoInline]
    list_display = ('ident','cliente', 'funcionario', 'data_chamado','data_realizacao','valor','observacao')
    list_filter = ['data_chamado','data_realizacao']
    search_fields = ['id']

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Servico, ServicoAdmin)
admin.site.register(Historico, HistoricoAdmin)