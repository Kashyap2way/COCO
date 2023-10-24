from gpiozero import Servo
from time import sleep

# Define pins for the 12 servos
servo_pins = [23, 25, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13]

# Create a list of 12 servo objects
servos = [Servo(pin) for pin in servo_pins]

try:
    while True:
        for servo in servos:
            servo.min()  # Set each servo to 45 degrees
            sleep(0.5)  # Wait for 1 second
            servo.mid()  # Set each servo to 90 degrees
            sleep(0.5)  # Wait for 1 second

except KeyboardInterrupt:
    # Clean up when the program is interrupted
    for servo in servos:
        servo.detach()

