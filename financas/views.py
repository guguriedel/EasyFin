from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
    
    return render(request, "home.html", {"form": form, "abrir_sheet": True}) #invalid volta pra home
