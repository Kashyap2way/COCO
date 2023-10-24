from gpiozero import Servo
from time import sleep

# Define pins for the 12 servos
servo_pins = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13]

# Create a list of 12 servo objects
servos = [Servo(pin) for pin in servo_pins]

# Set all servos to 90 degrees
for servo in servos:
    servo.mid()

try:
    while True:
        # Your code can go here, or you can leave the loop empty to keep the servos at 90 degrees.
        sleep(1)  # Sleep to reduce CPU usage

except KeyboardInterrupt:
    # Clean up when the program is interrupted
    for servo in servos:
        servo.detach()
