from flask import Flask, render_template
from flask_socketio import SocketIO
import cv2
from base64 import b64encode
import os


app = Flask(__name__)
socketio = SocketIO(app)
@app.route('/')
def index():
    generate_frames()
    return render_template('index.html')


def generate_frames():
    folder_path = 'image_folder'

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    camera = cv2.VideoCapture(0)
    
    while camera.isOpened():
        success, frame = camera.read()
        if success:
            image_filename = os.path.join(folder_path, f'frame_{time.time()}.jpg')
            cv2.imwrite(image_filename, frame)

            # Capture one image per second
            time.sleep(1)

    camera.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    socketio.run(app, debug=False)