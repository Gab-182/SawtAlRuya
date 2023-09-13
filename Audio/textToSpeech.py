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

def textToSpeech(text, filename):
    tts = gTTS(text)
    tts.save(filename + ".mp3")
    # os.system("open " + filename + ".mp3")
    return filename


def voiceChatWithPalm():
    while 1:
        textToSpeech(AIprompt(input("salemGPTVoice>")), "output")

textToSpeech("Your image is beign processed", "error")

# //python -m venv venv
# source venv/bin/activate
# pip install gTTS
# brew install mpg321
