from django.conf import settings
from django.db import models


class Categoria(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="categorias"
    )
    nome = models.CharField(max_length=50)
    teto = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True,
        help_text="Limite de gastos para esta categoria (opcional)",
    )

    class Meta:
        unique_together = ("usuario", "nome")
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nome


class Transacao(models.Model):
    class Tipo(models.TextChoices):
        ENTRADA = "ENTRADA", "Entrada"
        SAIDA = "SAIDA", "Saída"

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="transacoes"
    )
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name="transacoes"
    )
    descricao = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=7, choices=Tipo.choices, default=Tipo.SAIDA)
    data = models.DateField()
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-data", "-criado_em"]
        verbose_name_plural = "Transações"

    def __str__(self):
        return f"{self.descricao} - R$ {self.valor}"