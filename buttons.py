import cv2
import RPi.GPIO as GPIO
import time

# Pin Definitons:
led_pin = 13  # Board pin 12
but_pin = 15  # Board pin 15
dispH=960
dispW=1280
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
def main():
    # Pin Setup:
    GPIO.setmode(GPIO.BOARD)  # BOARD pin-numbering scheme
    GPIO.setup(led_pin, GPIO.OUT)  # LED pin set as output
    GPIO.setup(but_pin, GPIO.IN)  # button pin set as input

    # Initial state for LEDs:
    GPIO.output(led_pin, GPIO.HIGH)

    print("Starting demo now! Press CTRL+C to exit")
    i=1
    while i<10:
    	print("Waiting for button event")
    	x = GPIO.input(but_pin)
    	camera = cv2.VideoCapture(camSet)
    	print(x)
    	if x==1:
    		print("Button Pressed!",i)
    		i+=1
    		GPIO.output(led_pin, GPIO.LOW)
    		
    		return_value, image = camera.read()
    		cv2.imwrite(str(i+1)+'.png', image)
    		time.sleep(0.1)
    		GPIO.output(led_pin, GPIO.HIGH)
    		camera.release()
    	if i == 5 :
    		
    		camera.release()
    		GPIO.cleanup()  # cleanup all GPIOs

if __name__ == '__main__':
    main()

