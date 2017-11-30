from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^i18n/', include('django.conf.urls.i18n')),
                  url(r'^', include('webapp.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
