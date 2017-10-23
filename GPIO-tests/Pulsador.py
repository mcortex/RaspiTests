import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
count = 0
while True:
    inputValue = GPIO.input(24)
    if (inputValue == True):
        count = count + 1
        print("Boton presionado " + str(count) + " veces.")
        time.sleep(.3) #DEBOUNCE
    time.sleep(.01)
