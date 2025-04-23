

from flask import Flask, render_template, request, jsonify
from chatbot import ask_chatbot  # Make sure this is your Gemini-based chatbot


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    message = data.get("message", "")

    if not message:
        return jsonify({"response": "No message received."}), 400

    response = ask_chatbot(message)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
