import RPi.GPIO as gpio
from DriveMotor import *
import time

def init():
    gpio.setmode(gpio.BCM)
    motorL = DriveMotor(17,22)
    motorR = DriveMotor(23,24)
    startTime = time.time()

    while True:
        deltaTime = time.time() - startTime
        motorL.setPower(deltaTime/10 * 1.3)
        motorR.setPower(deltaTime/10)
        if deltaTime > 10:
            break

    motorL.setPower(0.0)
    motorR.setPower(0.0)

init()