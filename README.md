# fask-model

Sistema simples de login com Flask e sessão.

## Como executar no Windows PowerShell

Instale o Flask:

```powershell
pip install -r requirements.txt
```

Defina os dados usados para entrar:

```powershell
$env:LOGIN_CPF="coloque-o-cpf-aqui"
$env:LOGIN_SENHA="coloque-a-senha-aqui"
$env:FLASK_SECRET_KEY="coloque-uma-chave-secreta-aqui"
```

Execute o projeto:

```powershell
python app.py
```

Abra `http://127.0.0.1:5000` no navegador.

O sistema salva na sessão apenas o estado do login e o CPF. A senha não é guardada na sessão.
