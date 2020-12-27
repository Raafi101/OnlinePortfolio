from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/home/")
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/qualifications/")
def qualifications():
    return render_template("qualifications.html")

@app.route("/transcript/")
def transcript():
    return render_template("transcript.html")

@app.route("/accomplishments/")
def accomplishments():
    return render_template("accomplishments.html")

@app.route("/CSprojects/")
def CSprojects():
    return render_template("CSprojects.html")

@app.route("/CADprojects/")
def CADprojects():
    return render_template("CADprojects.html")

@app.route("/PSprojects/")
def PSprojects():
    return render_template("PSprojects.html")

@app.route("/GuitarProgress/")
def GuitarProgress():
    return render_template("GuitarProgress.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)