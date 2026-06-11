from datetime import date

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import redirect, render

from .forms import TransacaoForm

@login_required
def nova_transacao(request):
    if request.method != "POST":
        return redirect("home")

    form = TransacaoForm(request.POST, usuario=request.user)
    if form.is_valid():
        form.save(usuario=request.user)
        messages.success(request, "Transação salva com sucesso!") #Toas do db verde
        return redirect("home")

    # inválido: reabre a home com o sheet aberto, mostrando os erros.
    # Recalcula o dashboard pra ele não aparecer zerado durante o erro.
    hoje = date.today()
    do_mes = request.user.transacoes.filter(data__year=hoje.year, data__month=hoje.month)
    entradas = do_mes.filter(tipo="ENTRADA").aggregate(s=Sum("valor"))["s"] or 0
    saidas = do_mes.filter(tipo="SAIDA").aggregate(s=Sum("valor"))["s"] or 0
    return render(request, "home.html", {
        "form": form,
        "abrir_sheet": True,
        "is_entrada": form["tipo"].value() == "ENTRADA",
        "transacoes": request.user.transacoes.all()[:20],
        "entradas": entradas,
        "saidas": saidas,
        "saldo": entradas - saidas,
    })
