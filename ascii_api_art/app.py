from flask import Flask, request, jsonify
from main.ascii_service import generate_ascii_art

app = Flask(__name__)

@app.route("/ascii", methods = ["POST"])
def ascii_art():
    data = request.get_json
    text = data.get("text", "")
    font = data.get("font", "slant")
    if not text:
        return jsonify({"error": "Missing 'text' parametr"}), 400
    
    result = generate_ascii_art(text, font)
    return jsonify({"ascii" : result})

if __name__ == "__main__":
    app.run(debug=True)