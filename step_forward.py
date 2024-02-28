from gpiozero import Servo
from time import sleep

import numpy as np

Offset_s = 0 #Change offset values
Offset_e = 0 #Change offset values

#Link1: Length of link 1
#Link2: Length of link 2
#x_axis_dist: distance to be moved in X axis
#y_axis_dist: distance to be moved in Y axis


class Dog_Stride():
    def IK(self, LinkL1, LinkL2, x_axis_dist, y_axis_dist):
        cos_theta2 = (x_axis_dist**2 + y_axis_dist**2 - LinkL1**2 - LinkL2**2)/(2*LinkL1*LinkL2)
        theta2 = np.arccos(cos_theta2)

        theta1 = (np.arctan2(y_axis_dist, x_axis_dist)) - (np.arctan2(LinkL2*np.sin(theta2), (LinkL1 + LinkL2*np.cos(theta2))))

        theta1 = theta1 * (180/np.pi)
        theta2 = theta2 * (180/np.pi)

        return theta1, theta2
    
    def step_leg1(self, servo1, servo2):
        a1, a2 = self.IK(0.122, 0.13, 0, 0.1)
    
        # Set the servo angles for the first leg
        servo1.angle = 45
        servo2.angle = 120
        sleep(0.5)
    
        # Set the angles back to the calculated values for the first leg
        servo1.angle = a1
        servo2.angle = a2
        sleep(1)

        servo1.angle = 90
        servo2.angle = 90
        sleep(1)

    def step_leg2(self, servo1, servo2):
        # Define your Inverse Kinematics calculations for the second leg
        a1, a2 = self.IK(0.122, 0.13, 0, 0.1)  # Adjust the parameters as needed
    
        # Set the servo angles for the second leg
        servo1.angle = 135
        servo2.angle = 60
        sleep(0.5)
    
        # Set the angles back to the calculated values for the second leg
        servo1.angle = (180 - a1)
        servo2.angle = (180 - a2)
        sleep(1)

        servo1.angle = 90
        servo2.angle = 90
        sleep(1)

# Pins for the first leg
FRS_pin = 9
FLS_pin = 4
BRS_pin = 27
BLS_pin = 11

# Pins for the second leg
FRE_pin = 6
FLE_pin = 25
BRE_pin = 13
BLE_pin = 17

# Define servo objects for the first leg
servo1 = Servo(FRS_pin)
servo2 = Servo(FLS_pin)
servo3 = Servo(BRS_pin)
servo4 = Servo(BLS_pin)

# Define servo objects for the second leg
servo5 = Servo(FRE_pin)
servo6 = Servo(FLE_pin)
servo7 = Servo(BRE_pin)
servo8 = Servo(BLE_pin)

    # Stop the servos for the second leg
# You can call the 'step_leg1' and 'step_leg2' functions to perform movements for the two legs.


Dog_Stride = Dog_Stride()

while True:
    Dog_Stride.step_leg1(servo1, servo5)
    Dog_Stride.step_leg2(servo4, servo8)
    Dog_Stride.step_leg2(servo2, servo6)
    Dog_Stride.step_leg1(servo3, servo7)
