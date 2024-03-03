import cv2
from flask import Flask, Response
import multiprocessing

# Initialisiere Flask-App
app = Flask(__name__)

# Funktion, um den Video-Stream zu generieren
def generate_frames():
    video_capture = cv2.VideoCapture(2)
    while True:
        # Lies ein Frame von der Webcam
        success, frame = video_capture.read()
        if not success:
            break
        else:
            # Konvertiere das Frame in ein JPEG-Bild
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Route für den Video-Stream
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Funktion für den Webserver-Prozess
def run_flask():
    app.run(host='localhost', port=80, debug=True)


if __name__ == "__main__":
    # Starte den Flask-Server und den OpenCV-Prozess in separaten Prozessen
    flask_process = multiprocessing.Process(target=run_flask)
    flask_process.start()



    # Warte darauf, bis die Prozesse beendet sind
    flask_process.join()
