from django.views.generic import ListView
from webapp.models import Letter


class HomeView(ListView):
    template_name = 'home.html'
    model = Letter
