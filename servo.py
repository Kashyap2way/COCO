from gpiozero import Servo
from time import sleep

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
