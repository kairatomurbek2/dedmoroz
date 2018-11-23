from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget

from webapp.models import Letter, Organization, SantaClaus, HomeContent, HomeContentImages


class SantaClausAdmin(admin.ModelAdmin):
    list_per_page = 50
    search_fields = ['name', 'phone']
    list_display = ['name', 'phone', 'comments', 'comments_by_santa']
    readonly_fields = ('name', 'phone', 'comments_by_santa')


class SantaClausInline(admin.TabularInline):
    model = SantaClaus
    fields = ['name', 'phone']
    extra = 0


class LetterAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ['name', 'organization', 'age', 'status']
    search_fields = ['name']
    inlines = [SantaClausInline]
    list_filter = ['status', 'organization', 'age', 'grade']
    readonly_fields = ('date_create', )


class HomeContentForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = HomeContent
        fields = ['title', 'content']


class ImagesInline(admin.TabularInline):
    model = HomeContentImages
    fields = ['image']
    extra = 2


class HomeContentAdmin(admin.ModelAdmin):
    form = HomeContentForm
    inlines = [ImagesInline]

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


admin.site.register(Letter, LetterAdmin)
admin.site.register(Organization)
admin.site.register(SantaClaus, SantaClausAdmin)
admin.site.register(HomeContent, HomeContentAdmin)
admin.site.register(HomeContentImages)
