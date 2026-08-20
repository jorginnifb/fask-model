from flask import flask
app = flask(__name__)
@app_route("/")
def ota_mundo():
     return "olá, mundo! meu primeiro site com flask"
if __name__ == " __main__":
    app.run(debug= true)