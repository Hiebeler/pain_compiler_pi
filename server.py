from flask import Flask
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

PIN1 = 17
PIN2 = 27
GPIO.setmode(GPIO.BCM)  # or GPIO.BOARD, depending on your numbering scheme
GPIO.setup(PIN1, GPIO.OUT)  # Replace pin_number with the GPIO pin you're using
GPIO.setup(PIN2, GPIO.OUT)  # Replace pin_number with the GPIO pin you're using

@app.route("/")
def hello_world():
    shock(2)
    return "<p>Hello, World!</p>"

def shock(time):
    print("shocking")
    GPIO.output(PIN1, GPIO.HIGH)
    GPIO.output(PIN2, GPIO.HIGH)
    time.sleep(time)
    GPIO.output(PIN1, GPIO.LOW)
    GPIO.output(PIN2, GPIO.LOW)