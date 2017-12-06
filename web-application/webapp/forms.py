from django.utils.translation import ugettext_lazy as _
from django import forms

from webapp.models import SantaClaus


class CreateSantaClausForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': _("Ваше Имя")}))
    phone = forms.CharField(required=True,
                            widget=forms.NumberInput(attrs={'placeholder': _("Введите свой номер телефона")}))
    comments_by_santa = forms.CharField(label=_('Комментарий'), required=False,
                                        widget=forms.Textarea(
                                            attrs={'placeholder': _('Это поле не обязательно для заполнения')}))

    class Meta:
        model = SantaClaus
        fields = ['name', 'phone', 'comments_by_santa']
