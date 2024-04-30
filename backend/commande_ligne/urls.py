

from django.urls import path
from .views import CommandeligneView, CommandeligneCreateView

urlpatterns = [
    path('commande_ligne/', CommandeligneView.as_view(), name='Commandeligne-list'),
    path('commande_ligne/ajouter/', CommandeligneCreateView.as_view(), name='Commandeligne-create'),
]
