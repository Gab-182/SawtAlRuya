import os
from flask import Flask, jsonify
from textToSpeech import * 

app = Flask(__name__)

 
def generate_frames():
    return "hi this is test image description", "output.jpeg"

@app.route('/')
def index():
    text, filename = generate_frames()
    processed_audio_path = textToSpeech(text, filename)
    if os.path.exists(processed_audio_path):
        return jsonify({"success": True, "audio_url": processed_audio_path})
    else:
        return jsonify({"success": False, "error": "Audio file does not exist"})

if __name__ == "__main__":
    app.run(debug=True)
