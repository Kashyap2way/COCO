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

    pwm_b = (theta_b - 90)/90
    pwm_c = (theta_c - 90)/90

    return theta_b, theta_c, pwm_b, pwm_c

# Define pins for the 12 servos
servo_pins = [23, 25, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13]

# Create servo objects for each pin
servos = [Servo(pin) for pin in servo_pins]

# Define the angles
angle_90 = 0
angle_45 = -0.5  # Adjust this value if needed

try:
    while True:
        # Set all servos to 90 degrees
        for servo in servos:
            servo.value = angle_90

except KeyboardInterrupt:
    # Clean up when the program is terminated
    for servo in servos:
        servo.close()
