from flask import Flask, jsonify
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

PIN1 = 17
PIN2 = 27
PIN3 = 23
PIN4 = 24

GPIO.setmode(GPIO.BCM)  # or GPIO.BOARD, depending on your numbering scheme
GPIO.setup(PIN1, GPIO.OUT)  # Replace pin_number with the GPIO pin you're using
GPIO.setup(PIN2, GPIO.OUT)  # Replace pin_number with the GPIO pin you're using
GPIO.setup(PIN3, GPIO.OUT)  # Replace pin_number with the GPIO pin you're using
GPIO.setup(PIN4, GPIO.OUT) 

@app.route("/error", methods=["GET", "POST"])
def hello_world():
    shock(2)
    return "<p>Hello, World!</p>"

@app.route("/error2", methods=["GET", "POST"])
def hello_world():
    shock2(2)
    return "<p>Hello, World!</p>"

@app.route("/status")
def status():
    return jsonify({"status": "online", "message": "API is live"}), 200

def shock(seconds):
    print("shocking")
    GPIO.output(PIN1, GPIO.HIGH)
    GPIO.output(PIN2, GPIO.HIGH)
    time.sleep(seconds)
    GPIO.output(PIN1, GPIO.LOW)
    GPIO.output(PIN2, GPIO.LOW)

def shock2(seconds):
    print("shocking")
    GPIO.output(PIN3, GPIO.HIGH)
    GPIO.output(PIN4, GPIO.HIGH)
    time.sleep(seconds)
    GPIO.output(PIN3, GPIO.LOW)
    GPIO.output(PIN4, GPIO.LOW)