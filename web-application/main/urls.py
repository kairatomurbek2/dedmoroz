from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
                  path('jet/', include('jet.urls', 'jet')),
                  path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
                  path('admin/', admin.site.urls),
                  path('ckeditor/', include('ckeditor_uploader.urls')),
                  path('i18n/', include('django.conf.urls.i18n')),
                  path('', include('webapp.urls')),
                  path('robots.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
                  # url(r'^google3180cd19f46996bd.html$',
                  #     TemplateView.as_view(template_name="google3180cd19f46996bd.html",
                  #                          content_type="text/html")),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
