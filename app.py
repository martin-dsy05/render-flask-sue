from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "API funcionando en Railway - Despliegue continuo"

if __name__ == "__main__":
    app.run()
