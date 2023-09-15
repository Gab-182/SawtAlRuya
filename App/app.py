import os
import cv2
from flask import Flask, jsonify
from flask import Flask, send_from_directory, request
from flask import Flask, render_template 
from textToSpeech import textToSpeech
from flask import send_file
from transformers import pipeline

import openai
import os 
# Set your API key
api_key = os.environ.get('GPT')

# Initialize the OpenAI client
openai.api_key = api_key

# Example prompt for text generation
prompt = """who are you"""

# Generate text using the API
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=50  # Adjust the number of tokens as needed
)

# Print the generated text
print(response.choices[0].text)

#--------------------------------------------------------------------------------------------------------------

# app = Flask(__name__)
# app.static_folder = 'static'

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
    last_caption = None
    
    for caption in generate_frames():
        print(f"the caption is => [{caption}]")
        print(f"the last_caption is => [{last_caption}]")
        
        if caption != last_caption:
            processed_audio_path = textToSpeech(caption, 'frame.jpg')
            last_caption = caption
        else:
            processed_audio_path = None
        # yield processed_audio_path

#--------------------------------------------------------------------------------------------------------------

# Calling the audio files from Ahmed part
generate_audio_description()

#--------------------------------------------------------------------------------------------------------------

# error_audio = 'https://ideal-halibut-p4wvww97r5w2rqjv-5000.app.github.dev/static/error.mp3'

# @app.route('/')
# def index():
#     audio_url = next(generate_audio_description())
#     print(f"the audio url is => [{audio_url}]")
    
#     # Check if the processed audio file exists
#     if os.path.exists(audio_url):
#         audio_url = audio_url
#     else:
#         audio_url = error_audio

#     return render_template('home.html', audio_url=audio_url)

# if __name__ == "__main__":
#     app.run(debug=True)

#--------------------------------------------------------------------------------------------------------------
