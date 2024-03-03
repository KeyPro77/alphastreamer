import cv2
from django.http import StreamingHttpResponse
from django.shortcuts import render

global ret

def webcam_stream():

    cap = cv2.VideoCapture(1)
    global ret, frame
    while True:
        ret, frame = cap.read()

            


        
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


def webcam2(request):
    return StreamingHttpResponse(webcam_stream(), content_type='multipart/x-mixed-replace; boundary=frame')


def show_html(request):
    return render(request, 'home.html')
