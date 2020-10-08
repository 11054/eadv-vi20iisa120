### From the console> pip3 install flask

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my website"

if __name__ == "__main__":
    app.run(debug=True)