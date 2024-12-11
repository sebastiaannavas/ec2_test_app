from flask import Flask, request, jsonify, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/things")
def things():
    return jsonify({
        "payload":["foo","bar","baz","echo"]
    })

if __name__ == "__main__":
    app.run(debug=True)