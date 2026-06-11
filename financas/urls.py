from django.urls import path

from . import views

urlpatterns = [
    path("transacao/nova/", views.nova_transacao, name="nova_transacao"),
]