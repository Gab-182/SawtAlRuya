
# from flask import Flask, jsonify, send_from_directory
# import os

# app = Flask(__name__)
# UPLOAD_FOLDER = 'uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# @app.route('/')
# def index():
#     return send_from_directory('static', 'index.html')

# @app.route('/get_processed_audio')
# def get_processed_audio():
#     # Replace with logic to generate and provide the processed audio file's URL
#     processed_audio_url = 'path/to/processed/audio.mp3'
#     return jsonify({"success": True, "audio_url": processed_audio_url})

# if __name__ == "__main__":
#     app.run(debug=True)
# app.py
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
