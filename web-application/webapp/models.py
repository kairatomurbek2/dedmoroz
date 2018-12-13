from django.core.files.base import ContentFile
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import get_thumbnail
from ckeditor_uploader.fields import RichTextUploadingField

ACTIVE = 'AC'
MODERATION = 'MD'
DECLINE = 'DC'
ACCEPTED = 'AD'

STATUS_CHOICES = (
    (ACTIVE, _('Свободен')),
    (MODERATION, _('На расмотрение')),
    (DECLINE, _('Забронирован')),
    (ACCEPTED, _('Принят')),
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
    name = models.CharField(max_length=150, verbose_name=_('ФИО'), blank=True, null=True)
    age = models.IntegerField(blank=True, null=True, verbose_name=_('Возраст'))
    grade = models.IntegerField(verbose_name=_('Класс'), blank=True, null=True)
    image = models.ImageField(verbose_name=_("Письмо"), upload_to='images')
    status = models.CharField(choices=STATUS_CHOICES, max_length=2, default='AC', verbose_name=_('Статус'))
    organization = models.ForeignKey(Organization, related_name='letters', blank=True, null=True,
                                     on_delete=models.SET_NULL)
    date_create = models.DateField(verbose_name=_('Дата создании'), default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.id:
            super(Letter, self).save(*args, **kwargs)
            resized = get_thumbnail(self.image, "790x530")
            self.image.save(resized.name, ContentFile(resized.read()), True)
        super(Letter, self).save(*args, **kwargs)

    def get_next(self):
        next = Letter.objects.filter(id__gt=self.id)
        if next:
            return next.first()
        return False

    def get_prev(self):
        prev = Letter.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first()
        return False

    class Meta:
        verbose_name = _("Письмо")
        verbose_name_plural = _("Письма")


class SantaClaus(models.Model):
    letter = models.ForeignKey(Letter, related_name='santa_clauses', on_delete=models.CASCADE)
    name = models.CharField(max_length=250, verbose_name=_('Имя'))
    phone = models.CharField(max_length=20, verbose_name=_('Номер телефона'))
    comments = models.TextField(verbose_name=_('Комментарий'), blank=True, null=True)
    comments_by_santa = models.TextField(verbose_name=_('Комментарий от Деда Мороза'), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Дед Мороз")
        verbose_name_plural = _("Дед Морозы")


class HomeContent(models.Model):
    title = models.CharField(verbose_name=_('Заголовок'), max_length=100)
    content = RichTextUploadingField('awesome_ckeditor')

    class Meta:
        verbose_name = _('Контент на главной')
        verbose_name_plural = _('Контенты на главной')

    def __str__(self):
        return self.title


class HomeContentImages(models.Model):
    home_content = models.ForeignKey(HomeContent, related_name='home_content_images', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name=_("Изображение"), upload_to='contents')

    class Meta:
        verbose_name = _('Изображение')
        verbose_name_plural = _('изображения')
