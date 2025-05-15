from flask import Flask, request, jsonify
from main.storage import notes, add_note, delete_note_by_id

app = Flask(__name__)

@app.route("/notes", methods=["GET"])
def get_notes():
    return jsonify(notes)

@app.route("/notes", methods=["POST"])
def create_note():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({"error": "Misiing 'text' in request"}), 400
    note = add_note(data['text'])
    return jsonify(note), 201

@app.route("/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    success = delete_note_by_id(note_id)
    if not success:
        return jsonify({"error": "Note is not found"}), 404
    return jsonify({"message": "Note deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)