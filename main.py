from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Привіт! Веб-застосунок успішно розгорнуто на PaaS (Render).</h1><p>Виконав: Миколайчук Дмитро</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
