from django.db import models
from django.utils.translation import ugettext_lazy as _

ACTIVE = 'AC'
MODERATION = 'MD'
DECLINE = 'DC'

STATUS_CHOICES = (
    (ACTIVE, _('Свободен')),
    (MODERATION, _('На расмотрение')),
    (DECLINE, _('Забронирован')),
)


class Organization(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('Название организации'))
    street_address = models.CharField(max_length=350, verbose_name=_('Адрес организации'))
    phone = models.CharField(max_length=180, verbose_name=_('Номер телеофна организации'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Организация")
        verbose_name_plural = _("Организации")


class Letter(models.Model):
    image = models.ImageField(verbose_name=_("Письмо"), upload_to='images')
    status = models.CharField(choices=STATUS_CHOICES, max_length=2, default='AC', verbose_name=_('Статус'))
    organization = models.ForeignKey(Organization, related_name='letters', blank=True, null=True)

    def image_tag(self):
        return u'<img src="%s" width="200"/>' % self.image.url

    image_tag.short_description = _('Предварительный просмотр')
    image_tag.allow_tags = True

    class Meta:
        verbose_name = _("Письмо")
        verbose_name_plural = _("Письма")


class SantaClaus(models.Model):
    letter = models.ForeignKey(Letter, related_name='santa_clauses')
    name = models.CharField(max_length=250, verbose_name=_('Имя'))
    phone = models.CharField(max_length=20, verbose_name=_('Номер телефона'))
    comments = models.TextField(verbose_name=_('Коментарий'), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Дед Мороз")
        verbose_name_plural = _("Дед Морозы")
