from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import TemplateView
from webapp import forms
from webapp.models import Letter, SantaClaus, MODERATION


class HomeView(ListView):
    template_name = 'home.html'
    model = Letter
    ordering = '-pk'


class DetailLetterView(TemplateView):
    template_name = 'detail-letter.html'

    def get_context_data(self, **kwargs):
        context = super(DetailLetterView, self).get_context_data(**kwargs)
        context['letter'] = get_object_or_404(Letter, pk=self.kwargs['pk'])
        context['form'] = forms.CreateSantaClausForm
        return context


class CreateSantaClausView(CreateView):
    model = SantaClaus
    template_name = 'detail-letter.html'
    form_class = forms.CreateSantaClausForm

    def get_success_url(self):
        messages.add_message(self.request, messages.SUCCESS,
                             _("Спасибо! Наш волонтер свяжется с Вами в ближайшее время."))
        return reverse('home')

    def form_valid(self, form):
        santa = form.save(commit=False)
        letter = get_object_or_404(Letter, pk=self.kwargs['pk'])
        santa.letter = letter
        santa.save()
        letter.status = MODERATION
        letter.save()
        return super(CreateSantaClausView, self).form_valid(form)
