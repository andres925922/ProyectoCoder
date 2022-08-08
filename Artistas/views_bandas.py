from django.views.generic import DetailView
from .models import Banda
from Discos.models import Discos

class BandaDetail(DetailView):
    model = Banda
    template_name = "bandas_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        banda_id = self.kwargs['pk']
        context['discos'] = Discos.objects.filter(banda=banda_id)
        return context