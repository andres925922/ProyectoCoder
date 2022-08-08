from django.views.generic import DetailView
from .models import Banda

class BandaDetail(DetailView):
    model = Banda
    template_name = "bandas_detail.html"