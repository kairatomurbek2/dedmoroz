from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic import TemplateView

from webapp.models import Letter


class HomeView(ListView):
    template_name = 'home.html'
    model = Letter


class DetailLetterView(TemplateView):
    template_name = 'detail-letter.html'

    def get_context_data(self, **kwargs):
        context = super(DetailLetterView, self).get_context_data(**kwargs)
        context['letter'] = get_object_or_404(Letter, pk=self.kwargs['pk'])
        return context
