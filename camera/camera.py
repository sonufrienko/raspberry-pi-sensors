from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180
camera.resolution = (800, 600)
camera.framerate = 15

camera.start_preview()
camera.annotate_text = "Hello world!"
camera.start_recording('/home/pi/Desktop/video.h264')

sleep(5)

camera.capture('/home/pi/Desktop/2.jpg')
camera.stop_recording()
camera.stop_preview()
