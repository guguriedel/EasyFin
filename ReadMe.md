# EasyFin

Web app de organização financeira para jovens: registra gastos, mostra gráficos
da atividade financeira e permite criar tetos por categoria com alertas ao se
aproximar do limite.

> **Não é:** app mobile, sistema contábil para empresas, serviço de
> investimentos nem clone de planilha Excel.

## Stack

- Python 3.12 + Django
- PostgreSQL (produção) / SQLite (desenvolvimento inicial)
- Deploy: Vercel

## Como rodar localmente

```bash
# 1. Clonar e entrar na pasta
git clone https://github.com/guguriedel/EasyFin.git
cd eng_soft

# 2. Criar e ativar o ambiente virtual
python -m venv venv
.\venv\Scripts\Activate.ps1      # Windows (PowerShell)
# source venv/bin/activate       # Linux / macOS

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Aplicar migrações e subir o servidor
python manage.py migrate
python manage.py runserver
```
