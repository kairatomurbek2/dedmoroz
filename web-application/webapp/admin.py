from django.contrib import admin

from webapp.models import Letter, Organization, SantaClaus


class SantaClausAdmin(admin.ModelAdmin):
    list_per_page = 50
    search_fields = ['name', 'phone']
    list_display = ['name', 'phone', 'comments']
    readonly_fields = ('name', 'phone', 'comments_by_santa')


class SantaClausInline(admin.TabularInline):
    model = SantaClaus
    fields = ['name', 'phone']
    extra = 0


class LetterAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ['image_tag', 'status', 'organization']
    inlines = [SantaClausInline]
    list_filter = ['status', 'organization']


admin.site.register(Letter, LetterAdmin)
admin.site.register(Organization)
admin.site.register(SantaClaus, SantaClausAdmin)
