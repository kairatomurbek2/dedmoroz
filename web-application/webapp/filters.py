from django.utils.translation import ugettext_lazy as _

import django_filters

from webapp.models import STATUS_CHOICES


def assembly_status():
    choices = []
    for assembly_status in STATUS_CHOICES:
        choices.append(assembly_status)
    return choices


class StatusFilter(django_filters.FilterSet):
    status = django_filters.ChoiceFilter(label=_('Статус'), choices=assembly_status)
