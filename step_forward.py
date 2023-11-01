from gpiozero import Servo
from time import sleep

import numpy as np


#Link1: Length of link 1
#Link2: Length of link 2
#x_axis_dist: distance to be moved in X axis
#y_axis_dist: distance to be moved in Y axis

def IK(LinkL1, LinkL2, x_axis_dist, y_axis_dist):
    cos_theta2 = (x_axis_dist**2 + y_axis_dist**2 - LinkL1**2 - LinkL2**2)/(2*LinkL1*LinkL2)
    theta2 = np.arccos(cos_theta2)

    theta1 = (np.arctan2(y_axis_dist, x_axis_dist)) - (np.arctan2(LinkL2*np.sin(theta2), (LinkL1 + LinkL2*np.cos(theta2))))

    theta1 = theta1 * (180/np.pi)
    theta2 = theta2 * (180/np.pi)

    return (theta1-90)/90, (theta2-90)/90

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

def step_leg1():
    a1, a2 = IK(0.122, 0.13, 0, 0.1)
    
    # Set the servo angles for the first leg
    servo1.value = -0.5
    servo5.value = 0.33
    sleep(0.5)
    
    
    # Set the angles back to the calculated values for the first leg
    servo1.value = a1
    servo5.value = a2
    sleep(0.5)
    

def step_leg2():
    # Define your Inverse Kinematics calculations for the second leg
    a1, a2 = IK(0.122, 0.13, 0, 0.1)  # Adjust the parameters as needed
    
    # Set the servo angles for the second leg
    servo3.value = -0.5
    servo7.value = 0.33
    sleep(0.5)
    
    # Set the angles back to the calculated values for the second leg
    servo3.value = a1
    servo7.value = a2
    sleep(0.5)
    
    # Stop the servos for the second leg
# You can call the 'step_leg1' and 'step_leg2' functions to perform movements for the two legs.

try:
    while True:
        step_leg1()
        sleep(0.5)
        servo1.value = 90
        servo5.value = 90
        sleep(1)
        step_leg2()
        sleep(0.5)
        servo3.value = 90
        servo7.value = 90   

except KeyboardInterrupt:
    # Clean up when the program is terminated
    for servo in servos:
        servo.close()
