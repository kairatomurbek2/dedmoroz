from django.conf.urls import url
from webapp.views import HomeView, DetailLetterView, CreateSantaClausView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^letters/(?P<pk>\d+)/$', DetailLetterView.as_view(), name="letter_detail"),
    url(r'^letters/(?P<pk>\d+)/create/$', CreateSantaClausView.as_view(), name="create_santa"),
]
