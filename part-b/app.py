
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("demo-dev.html", color="purple")


@app.route("/production")
def production():
    return render_template("demo-production.html", color="purple")


if __name__ == "__main__":
    app.run(debug=True)
