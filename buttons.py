
import RPi.GPIO as GPIO
import time

# Pin Definitons:
led_pin = 13  # Board pin 12
but_pin = 15  # Board pin 15

def main():
    # Pin Setup:
    GPIO.setmode(GPIO.BOARD)  # BOARD pin-numbering scheme
    GPIO.setup(led_pin, GPIO.OUT)  # LED pin set as output
    GPIO.setup(but_pin, GPIO.IN)  # button pin set as input

    # Initial state for LEDs:
    GPIO.output(led_pin, GPIO.LOW)

    print("Starting demo now! Press CTRL+C to exit")
    try:
        while True:
        	print("Waiting for button event")
        	x = GPIO.input(but_pin)
        	print(x)
        	if x==1:
        		print("Button Pressed!")
        		GPIO.output(led_pin, GPIO.HIGH)
        		time.sleep(1)
        		GPIO.output(led_pin, GPIO.LOW)
    finally:
        GPIO.cleanup()  # cleanup all GPIOs

if __name__ == '__main__':
    main()
