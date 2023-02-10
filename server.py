from flask import Flask
from flask import render_template
from datetime import datetime as dt

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", year=dt.now().year)


if __name__ == "__main__":
    app.run(debug=True)
