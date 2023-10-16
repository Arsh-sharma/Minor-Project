from flask import Flask, request, jsonify, render_template
from keras.models import model_from_json
import os

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    if request.method == "GET":
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)