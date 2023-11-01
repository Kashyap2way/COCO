from math import *
from gpiozero import Servo
from time import sleep

def stand(hypo):
    hypo = hypo/1000
    cos_theta_b = (0.122**2 + hypo**2 - 0.130**2)/(2*0.122*hypo)

    theta_b = int(degrees(acos(cos_theta_b)))
    theta_c = (180-(theta_b*2))
    
    theta_b += 52
    theta_c -= 14

    return theta_b, theta_c

def conversion(angle):
    pwm = (angle - 90)/90
    return pwn

# Define pins for the 12 servos
#servo_pins = [23, 25, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13

FRS_servo = Servo(9)
FLS_servo = Servo(4)
BRS_servo = Servo(27)
BLS_servo = Servo(11)
FRE_servo = Servo(6)
FLE_servo = Servo(25)
BRE_servo = Servo(13)
BLE_servo = Servo(17)

# Create servo objects for each pin
#servos = [Servo(pin) for pin in servo_pins]

# Define the angles
#angle_90 = 0
#angle_45 = -0.5  # Adjust this value if needed

try:
    while True:
        # Set all servos to 90 degrees
        
        FRS_servo_value, FRE_servo_value = stand(150)
        FRS_servo.value = conversion(FRS_servo_value + 20)
        FRE_servo.value = conversion(FRE_servo_value)
        sleep(0.5)

        FRS_servo_value, FRE_servo_value = stand(200)
        FRS_servo.value = conversion(FRS_servo_value + 20)
        FRE_servo.value = conversion(FRE_servo_value)
        sleep(0.5)


