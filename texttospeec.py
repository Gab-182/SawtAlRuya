from gtts import gTTS
import os
from PIL import Image
import google.generativeai as palm
import os
import sys


palm.configure(api_key=os.environ.get('PALM'))


def preparePrompt(logs):
    return ("Please help me explian this logs to person with blindnes his name is TOM")


def AIprompt(msg):
    response = palm.chat(messages=msg)
    return response.last
# Text you want to convert to speech

# Create a gTTS object



def voiceChatWithPalm():
    while 1:
        txt = input("salemGPTVoice>")
        text = AIprompt(txt)
        tts = gTTS(text)
        tts.save("output.mp3")
        os.system("open output.mp3")  # Example for Linux


# //python -m venv venv
# source venv/bin/activate
# pip install gTTS
# brew install mpg321
