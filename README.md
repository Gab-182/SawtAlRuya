# SawtAlRuya
Computer vision hackathon project
-------------
## Image Captioning with Transformers

This project utilizes the Hugging Face Transformers library to perform image captioning using the Salesforce/blip-image-captioning-base model. It captures images from a webcam, generates image captions, and displays the results.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Gab-182/SawtAlRuya
   ```
2. Navigate to the project directory:
   ```bash
   cd image-captioning
   ```
3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment (Linux/Mac):
   ```bash
   source venv/bin/activate
   ```
5. pip install -r requirements.txt

------------

### Usage:

- Run the image captioning script:
   ```bash
   python image_captioning.py
   ```
   
To exit the script, press ```Ctrl + C```

### What to Expect

The script will initialize the image captioning model using the Salesforce/blip-image-captioning-base model.

It will create a folder named image_folder to store captured images.

The script will continuously capture images from your webcam, generate image captions, and print them to the terminal.

Each caption will be printed in the format:
```
[{'generated_text': 'a woman is kneeling on the ground'}]
```

