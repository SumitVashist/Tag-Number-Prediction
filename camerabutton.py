import cv2
import RPi.GPIO as GPIO
import traceback

dispH=960
dispW=1280
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
but_pin = 15  # Board pin 15
GPIO.setmode(GPIO.BOARD)  # BOARD pin-numbering scheme
GPIO.setup(but_pin, GPIO.IN)  # button pin set as input
print("Starting demo now! Press CTRL+C to exit")

i = 1

try:
	while i<2:
		value = GPIO.input(but_pin)
		#print(type(value))
		print("Value read from pin {} : {}".format(but_pin, value))
		if value ==1:
			#print("assfcdgsdg")
			
			camera = cv2.VideoCapture(camSet)
			return_value, image = camera.read()
			cv2.imwrite(str(i+1)+'.png', image)
			cv2.imshow("Image",image)
			i+=1
			camera.release()
			cv2.destroyAllWindows()
			break		
except:
    print(traceback.format_exc())
finally:
	GPIO.cleanup()
	camera.release()
	cv2.destroyAllWindows()

	
	



