from django.urls import path
from webapp.views import HomeView, DetailLetterView, CreateSantaClausView

urlpatterns = [
    path(r'', HomeView.as_view(), name='home'),
    path('letters/<int:id>/', DetailLetterView.as_view(), name="letter_detail"),
    path('letters/<int:id>/create/$', CreateSantaClausView.as_view(), name="create_santa"),
]
