from transformers import pipeline
import cv2
import os

# Initialize the image captioning model
captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

# Create a generator function to capture and yield captions
def generate_frames(captioner):
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



#------------------------------------------------------------------------------------------
# Testing
#------------------------------------------------------------------------------------------

# def capture_and_print_captions():
#     for captions in generate_frames():
#         print(captions)

# capture_and_print_captions()

#------------------------------------------------------------------------------------------
