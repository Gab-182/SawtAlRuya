import os
import cv2
from flask import Flask, jsonify
from flask import Flask, send_from_directory, request
from flask import Flask, render_template 
from textToSpeech import textToSpeech
from flask import send_file
from transformers import pipeline

#--------------------------------------------------------------------------------------------------------------

app = Flask(__name__)
app.static_folder = 'static'

#--------------------------------------------------------------------------------------------------------------

# Initialize the image captioning model
captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

#--------------------------------------------------------------------------------------------------------------
# this function will generate the captions from the frames and return a generator object that include 
# the captions

def generate_frames():
    camera = cv2.VideoCapture(0)
    
    try:
        while True:
            success, frame = camera.read()
            if success:
                image_filename = 'frame.jpg'
                cv2.imwrite(image_filename, frame)
                
                # Perform image captioning on the captured image
                captions = captioner(image_filename)
                captions = captions[0]['generated_text']

                # Yield the generated captions
                yield captions

                # Delete the image after processing it
                os.remove(image_filename)

    except KeyboardInterrupt:
        pass
    finally:
        camera.release()
        cv2.destroyAllWindows()

#--------------------------------------------------------------------------------------------------------------

# This function will generate the audio description from the text, and return a generator object that include the 
# path of the audio file

def generate_audio_description():
    for caption in generate_frames():
        print(f"the caption is => [{caption}]")
        # textToSpeech(caption, 'frame')
        
        processed_audio_path = textToSpeech(caption, 'frame.jpg')
        yield processed_audio_path

#--------------------------------------------------------------------------------------------------------------

error_audio = 'https://ideal-halibut-p4wvww97r5w2rqjv-5000.app.github.dev/static/error.mp3'

@app.route('/')
def index():
    audio_url = next(generate_audio_description())  # Get the audio URL from the generator
    # Check if the processed audio file exists
    if os.path.exists(audio_url):
        audio_url = audio_url
    else:
        audio_url = error_audio

    return render_template('home.html', audio_url=audio_url)

if __name__ == "__main__":
    app.run(debug=True)

#--------------------------------------------------------------------------------------------------------------