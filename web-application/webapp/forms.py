from django.utils.translation import ugettext_lazy as _
from django import forms

from webapp.models import SantaClaus


class CreateSantaClausForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': _("Ваше Имя")}))
    phone = forms.CharField(required=True,
                            widget=forms.NumberInput(attrs={'placeholder': _("Введите свой номер телефона")}))

    class Meta:
        model = SantaClaus
        fields = ['name', 'phone']
