from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def ola_mundo():
    return render_template("login.html")

@app.route("/painel")
def painel():
    return render_template("painel.html")

if __name__ == "__main__":
    app.run(debug=True) 