from DriveMotor import *
import time
import math

class RobotPosition:
    # Links to drive motors:
    motorL = 0 # type: DriveMotor
    motorR = 0 # type: DriveMotor

    # this is the current position in world coordinates
    positionX = 0
    positionY = 0
    angle = 0

    # CONSTANTS
    # if one motor is at 100% power and the other is off, how many radians per second will we be going
    speedPerSteering = 3.5
    maxSpeed = 55


    # the last time update was called
    lastUpdateTime = 0
    # the amount of time that elapsed between the current and last update
    deltaTime = 0

    # RobotPosition only requires the links to the two motors
    def __init__(self, motorL, motorR):
        self.motorL = motorL
        self.motorR = motorR

    # call this every loop update
    def update(self):
        currentTime = time.time()
        self.deltaTime = currentTime - self.lastUpdateTime
        self.lastUpdateTime = currentTime

        self.updatePosition()

    # calculates our new position
    def updatePosition(self):
        # first we will get the powers of the two motors
        leftPower = self.motorL.getPower()
        rightPower = self.motorR.getPower()


        # estimate our current velocity
        currentVelocity = (leftPower + rightPower) / 2

        # amount steering is positive when we are turning left (angle increasing)
        amountSteering = rightPower - leftPower
        # if one motor is maxed out on power and the other zero, it will go 3.5 radians per second
        currentAngularVelocity = amountSteering * self.speedPerSteering

        # now we can increment our angle
        self.angle += currentAngularVelocity * self.deltaTime

        # increment our current position
        self.positionX += math.cos(self.angle) * currentVelocity
        self.positionY += math.sin(self.angle) * currentVelocity

