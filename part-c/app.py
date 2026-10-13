
from flask import Flask, render_template

app = Flask(__name__)

plans = [
    {
        "name": "Starter",
        "price": "$0",
        "description": "For getting started",
        "features": ["Basic features", "Community support"],
        "button": "Get started"
    },
    {
        "name": "Pro",
        "price": "$19",
        "description": "For growing teams",
        "features": ["All Starter features", "Priority support"],
        "button": "Start Pro"
    },
    {
        "name": "Business",
        "price": "$49",
        "description": "For established teams",
        "features": ["All Pro features", "Team management"],
        "button": "Contact sales"
    }
]

@app.route("/")
def home():
    return render_template("pricing.html", plans=plans)


@app.route("/apply")
def apply_version():
    return render_template("pricing-apply.html", plans=plans)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
