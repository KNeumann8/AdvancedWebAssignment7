#cool
from gpiozero import LED, Button
from picamera import PiCamera
from datetime import datetime

camera = PiCamera()
led_yellow = LED(12)
button_yellow = Button(4)
led_blue = LED(13)
button_green = Button(5)

#While the program is running the blue
#light will shine
loopControl = True
camera.start_preview()
led_blue.on()

while loopControl:
    if(button_green.is_pressed):
        loopControl = False
    if(button_yellow.is_pressed):
        now = datetime.now()
        now = now.strftime("%m|%d|%Y,%H:%M:%S")
        camera.annotate_text = now
        camera.capture('/home/pi/Desktop/MyPictures<3/' + now + '.jpg')
        led_yellow.on()
        led_yellow.off()

#When the program stops, the blue light turns off
led_blue.off()
camera.stop_preview()
quit()

