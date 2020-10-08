### From the console> pip3 install flask

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")
    return "Hello! This is the main page <h1>Hello<h1>"

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/hack/')
def hack():
    return render_template("hack.html")


if __name__ == "__main__":
    app.run(debug=True)
