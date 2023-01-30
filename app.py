from flask import Flask, redirect, render_template, request

# Create application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/profil")
def profil():
    return render_template("profil.html")


@app.route("/kontakt", methods=["GET", "POST"])
def kontakt():
    return render_template("kontakt.html")
