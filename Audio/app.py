
# from flask import Flask, jsonify
# from textToSpeech import * 

# app = Flask(__name__)

 
# def generate_frames():
#     return "hi this is test image description", "output.jpeg"

# @app.route('/')
# def index():
#     text, filename = generate_frames()
#     processed_audio_path = textToSpeech(text, filename)
#     error_audio = 'error.mp3'
#     if os.path.exists(processed_audio_path):
#         return jsonify({"success": True, "audio_url": processed_audio_path})
#     else:
#         return jsonify({"success": False, "error": error_audio})

# if __name__ == "__main__":
#     app.run(debug=True)

import os
from flask import Flask, jsonify
from flask import Flask, send_from_directory, request
from textToSpeech import textToSpeech  # Assuming you have a textToSpeech function

app = Flask(__name__)

# Placeholder function for generating text and an image filename
def generate_frames():
    text = "hi this is test image description"
    filename = "output.jpeg"
    return text, filename

def generate_audio_description():
    text, filename = generate_frames()
    processed_audio_path = textToSpeech(text, filename)  # Assuming this function creates the audio file
    return processed_audio_path

@app.route('/')
def serve_content():
    if 'audio/mpeg' in request.headers.get('Accept', ''):
        processed_audio_path = generate_audio_description()
        error_audio = 'static/error.mp3'
        
        # Check if the processed audio file exists
        if os.path.exists(processed_audio_path):
            return send_from_directory(os.path.dirname(processed_audio_path), os.path.basename(processed_audio_path))
        else:
            return send_from_directory(os.path.dirname(error_audio), os.path.basename(error_audio))
    else:
        return send_from_directory('static', 'index.html')

if __name__ == "__main__":
    app.run(debug=True)
