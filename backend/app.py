from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json
from models.sentiment_model import SentimentModel
from models.tip_generator import TipGenerator

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:5173", "http://127.0.0.1:5173"]}})

print("Loading models (this may take a bit)...")
sent_model = SentimentModel()
tip_gen = TipGenerator()
print("Models loaded.")

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

JOURNALS_PATH = os.path.join(DATA_DIR, "journals.json")
if not os.path.exists(JOURNALS_PATH):
    with open(JOURNALS_PATH, "w", encoding="utf-8") as f:
        json.dump([], f)

def save_entry(entry):
    with open(JOURNALS_PATH, "r+", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []
        data.append(entry)
        f.seek(0)
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.truncate()

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/analyze", methods=["POST"])
def analyze():
    payload = request.json
    if not payload or "text" not in payload:
        return jsonify({"error": "no text provided"}), 400

    text = payload.get("text", "").strip()
    save_flag = payload.get("save", True)
    excerpt = text[:500]

    emotion, scores = sent_model.predict_emotion(text)
    tip = tip_gen.generate_tip(emotion, excerpt)

    result = {"emotion": emotion, "scores": scores, "tip": tip}

    if save_flag:
        from datetime import datetime
        entry = {
            "text": text,
            "emotion": emotion,
            "scores": scores,
            "tip": tip,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
        save_entry(entry)

    return jsonify(result)

@app.route("/history", methods=["GET"])
def history():
    with open(JOURNALS_PATH, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = []
    return jsonify({"entries": data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
