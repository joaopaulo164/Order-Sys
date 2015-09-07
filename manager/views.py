from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Cliente, Funcionario, Historico, Servico

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'manager/index.html'
    context_object_name = 'all_historico_list'

    def get_queryset(self):
        """Return all."""
        return Historico.objects.all()

class DetailView(generic.DetailView):
    model = Historico
    template_name = 'manager/historico_detail.html'


class ResultsView(generic.DetailView):
    model = Historico
    template_name = 'manager/results.html'

# def vote(request, historico_id):
#     h = get_object_or_404(Historico, pk=historico_id)
#     try:
#         select_services = h.servico_set.get(pk=request.POST['servico'])
#     except (KeyError, Servico.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'manager/historico_detail.html', {
#             'historico': h,
#             'error_message': "Você não selecionou uma servico.",
#         })
#     else:
#         select_services.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('manager:results', args=(h.id,)))