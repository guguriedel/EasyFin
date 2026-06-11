from django.urls import path

from . import views

urlpatterns = [
    path("transacao/nova/", views.nova_transacao, name="nova_transacao"),
    path("transacao/<int:pk>/excluir", views.excluir_transacao, name="excluir_transacao"),
    path("transacao/<int:pk>/editar", views.editar_transacao, name="editar_transacao"),

]