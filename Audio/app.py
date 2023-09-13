
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
from textToSpeech import textToSpeech  # Assuming you have a textToSpeech function

app = Flask(__name__)

# Placeholder function for generating text and an image filename
def generate_frames():
    text = "hi this is test image description"
    filename = "output.jpeg"
    return text, filename

def generate_audio_description():
    text, filename = generate_frames()
    processed_audio_path = textToSpeech(text, filename)
    return processed_audio_path

@app.route('/')
def index():
    processed_audio_path = generate_audio_description()
    error_audio = 'error.mp3'
    
    # Check if the processed audio file exists
    if os.path.exists(processed_audio_path):
        audio_url = processed_audio_path
    else:
        audio_url = error_audio

    return jsonify({"success": True, "audio_url": audio_url})

if __name__ == "__main__":
    app.run(debug=True)

