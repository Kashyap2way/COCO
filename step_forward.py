from gpiozero import Servo
from time import sleep
import Inverse_Kinematics as ik

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
    a1, a2 = ik.IK(0.122, 0.13, 0, 0.1)
    
    # Set the servo angles for the first leg
    servo1.angle = 45
    servo5.angle = 120
    sleep(0.5)
    
    # Stop the servos for the first leg
    servo1.angle = None
    servo5.angle = None
    
    # Set the angles back to the calculated values for the first leg
    servo1.angle = a1
    servo5.angle = a2
    sleep(0.5)
    
    # Stop the servos for the first leg
    servo1.angle = None
    servo5.angle = None

def step_leg2():
    # Define your Inverse Kinematics calculations for the second leg
    a1, a2 = ik.IK(0.122, -0.13, 0, 0.1)  # Adjust the parameters as needed
    
    # Set the servo angles for the second leg
    servo3.angle = 45
    servo7.angle = 120
    sleep(0.5)
    
    # Stop the servos for the second leg
    servo3.angle = None
    servo7.angle = None
    
    # Set the angles back to the calculated values for the second leg
    servo3.angle = a1
    servo7.angle = a2
    sleep(0.5)
    
    # Stop the servos for the second leg
    servo3.angle = None
    servo7.angle = None

# You can call the 'step_leg1' and 'step_leg2' functions to perform movements for the two legs.


while True:
    step_leg1()
    servo1.angle = 90
    servo5.angle = 90
    sleep(1)
    step_leg2()  # Corrected the function call
    servo3.angle = 90  # Corrected the angle setting
    servo7.angle = 90  # Corrected the angle setting
    sleep(1)  
