#Import the necessary modules.
from flask import Flask, render_template
from os import environ

# Instantiate an 'app' object.
app = Flask(__name__)

# Assign a decorator to the default URL.
@app.route("/")
def index(): # define the default URL as the index.
    return render_template("index.html")

# run the app.
if __name__ == "__main__":
    port = int(environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
