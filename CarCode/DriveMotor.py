from gpiozero import Motor

class DriveMotor:
    myMotor = 0
    pin1 = 0
    pin2 = 0
    currentPower = 0

    # requires the two gpio pins
    def __init__(self, pin1, pin2):
        self.pin1 = pin1
        self.pin2 = pin2
        self.myMotor = Motor(pin1, pin2)

    # Use this to change the motor power
    def setPower(self, power):
        self.currentPower = power
        if power > 0:
            self.myMotor.forward(power)
        else:
            self.myMotor.backward(-power)

    # get's the current power of the motor
    def getPower(self):
        return self.currentPower