from django.contrib import admin

from webapp.models import Letter, Organization, SantaClaus


class SantaClausAdmin(admin.ModelAdmin):
    list_per_page = 50
    search_fields = ['name', 'phone']
    list_display = ['name', 'phone']
    readonly_fields = ('name', 'phone')


admin.site.register(Letter)
admin.site.register(Organization)
admin.site.register(SantaClaus, SantaClausAdmin)
