from transformers import pipeline
import cv2
import time
import os

# Initialize the image captioning model
captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

# Create a folder to store captured images
folder_path = 'image_folder'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Create a generator function to capture and yield captions
def generate_captions():
    camera = cv2.VideoCapture(0)
    
    try:
        while True:
            success, frame = camera.read()
            if success:
                image_filename = os.path.join(folder_path, f'frame.jpg')
                cv2.imwrite(image_filename, frame)
                
                # Perform image captioning on the captured image
                captions = captioner(image_filename)

                # Yield the generated captions
                yield captions

                # Delete the image after processing it
                os.remove(image_filename)

                # Capture one image per second
                # time.sleep(0.5)

    except KeyboardInterrupt:
        pass
    finally:
        camera.release()
        cv2.destroyAllWindows()

# Function to capture and print captions
def capture_and_print_captions():
    for captions in generate_captions():
        # Print the generated captions
        print(captions)

# Call the function to start capturing and printing captions
capture_and_print_captions()