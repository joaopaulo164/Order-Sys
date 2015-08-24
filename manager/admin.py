from django.contrib import admin

from .models import Cliente, Funcionario, Historico, Servico
# Register your models here.

class ServicoInline(admin.TabularInline):
    model = Servico
    extra = 0

class HistoricoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Historico',               {'fields': ['cliente', 'funcionario','data_chamado','data_realizacao','valor_total']}),
        ('Informacoes', {'fields': ['observacao'], 'classes': ['collapse']}),
    ]
    inlines = [ServicoInline]
    list_display = ('ident','cliente', 'funcionario', 'data_chamado','data_realizacao','valor_total','observacao')
    list_filter = ['data_chamado','data_realizacao']
    search_fields = ['cliente','funcionario']

admin.site.register(Cliente)
admin.site.register(Funcionario)
admin.site.register(Historico,HistoricoAdmin)