from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
                  url(r'^jet/', include('jet.urls', 'jet')),
                  url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
                  url(r'^admin/', admin.site.urls),
                  url(r'^i18n/', include('django.conf.urls.i18n')),
                  url(r'^', include('webapp.urls')),
                  url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
                  url(r'^google8d646686634b60ab.html$',
                      TemplateView.as_view(template_name="google3180cd19f46996bd.html",
                                           content_type="text/html")),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
