import os
import secrets

from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or secrets.token_hex(32)


@app.route("/", methods=["GET", "POST"])
def login():
    erro = None

    if request.method == "POST":
        cpf = request.form.get("cpf", "").strip()
        senha = request.form.get("senha", "")

        cpf_correto = os.environ.get("LOGIN_CPF")
        senha_correta = os.environ.get("LOGIN_SENHA")

        if not cpf_correto or not senha_correta:
            erro = "Configure LOGIN_CPF e LOGIN_SENHA antes de entrar."
        elif cpf == cpf_correto and senha == senha_correta:
            session["usuario_logado"] = True
            session["cpf"] = cpf
            return redirect(url_for("painel"))
        else:
            erro = "CPF ou senha incorretos."

    return render_template("login.html", erro=erro)


@app.route("/painel")
def painel():
    if not session.get("usuario_logado"):
        return redirect(url_for("login"))

    return render_template("painel.html", cpf=session["cpf"])


@app.route("/sair")
def sair():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
