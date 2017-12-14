from django.contrib import admin

from webapp.models import Letter, Organization, SantaClaus


class SantaClausAdmin(admin.ModelAdmin):

    def letter(self):
        html = ""
        for obj in Letter.objects.filter(santa_clauses=self.id):
            html += '<p><a href="/admin/webapp/letter/%s/change"><img src="%s" width="200"/></a></p>' % (obj.id, obj.image.url)
        return html
    letter.allow_tags = True

    list_per_page = 50
    search_fields = ['name', 'phone']
    list_display = ['name', 'phone', 'comments', 'comments_by_santa', letter]
    readonly_fields = ('name', 'phone', 'comments_by_santa')


class SantaClausInline(admin.TabularInline):
    model = SantaClaus
    fields = ['name', 'phone']
    extra = 0


class LetterAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ['image_tag', 'status', 'organization']
    search_fields = ['name']
    inlines = [SantaClausInline]
    list_filter = ['status', 'organization', 'birthday', 'grade']


admin.site.register(Letter, LetterAdmin)
admin.site.register(Organization)
admin.site.register(SantaClaus, SantaClausAdmin)
