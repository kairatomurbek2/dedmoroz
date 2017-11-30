from django import template
from django.template import TemplateDoesNotExist

register = template.Library()


@register.simple_tag
def uikit_alert_class(tags):
    if tags == 'error':
        tags = 'danger'

    return tags
