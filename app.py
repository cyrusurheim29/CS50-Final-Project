from flask import Flask, render_template, jsonify, flash, redirect, request, session
from cs50 import SQL
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///web_scraping/volopps.db")

# Google Maps API key
GOOGLE_MAPS_API_KEY = "AIzaSyCLP7ugaKpJVaW79mHe6Fesj00KycMdvWM"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("map.html", api_key=GOOGLE_MAPS_API_KEY)
    else:
        return render_template("map.html", api_key=GOOGLE_MAPS_API_KEY)

@app.route("/data")
def data():
    """Fetch volunteer opportunities from the database."""
    opportunities = db.execute("SELECT name, address, webpage, classification FROM volunteer_opportunities")
    return jsonify(opportunities)

@app.route("/aboutus.html", methods=["GET", "POST"])
def aboutus():
    if request.method == "GET":
        return render_template("aboutus.html", api_key=GOOGLE_MAPS_API_KEY)
    else:
        return render_template("aboutus.html", api_key=GOOGLE_MAPS_API_KEY)

@app.route("/contribute.html", methods=["GET", "POST"])
def contribute():
    if request.method == "POST":
        # Get form data
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # Validate form data
        if not name or not email or not message:
            flash("All fields are required!", "danger")
            return redirect("/contribute.html")

        # Redirect to mailto link
        mailto_link = f"mailto:cyrusurheim@college.harvard.edu?subject=New%20Contribution%20to%20Equal%20Opportunity%20Boston&body=Name:%20{name}%0AEmail:%20{email}%0AMessage:%20{message}"
        
        # Redirect user to their email client with pre-filled message
        return redirect(mailto_link)

    return render_template("contribute.html")

@app.route("/datasets.html", methods=["GET", "POST"])
def datasets():
    if request.method == "GET":
        return render_template("datasets.html", api_key=GOOGLE_MAPS_API_KEY)
    else:
        return render_template("datasets.html", api_key=GOOGLE_MAPS_API_KEY)

if __name__ == "__main__":
    app.run(debug=True)
