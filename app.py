from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

HF_API_KEY = os.getenv("HF_API_KEY")
MODEL_URL = "https://api-inference.huggingface.co/models/your-model-name"

@app.route("/")
def home():
    return "Backend Running Successfully!"

@app.route("/generate", methods=["POST"])
def generate_video():
    text = request.json.get("text")
    duration = request.json.get("duration")

    payload = {
        "inputs": text,
        "parameters": {
            "duration": int(duration)
        }
    }

    headers = {"Authorization": f"Bearer {HF_API_KEY}"}

    response = requests.post(MODEL_URL, headers=headers, json=payload)

    try:
        result = response.json()
        return jsonify(result)
    except:
        return jsonify({"error": "Invalid Response"})


if __name__ == "__main__":
    app.run()
