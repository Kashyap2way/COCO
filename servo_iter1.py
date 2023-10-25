import RPi.GPIO as GPIO
from time import *

GPIO.setmode(GPIO.BCM)

servo_pin1 = 9
servo_pin2 = 6

GPIO.setup(servo_pin1, GPIO.OUT)
GPIO.setup(servo_pin2, GPIO.OUT)

pwm1 = GPIO.PWM(servo_pin1, 50)
pwm2 = GPIO.PWM(servo_pin2, 50)

def set_angle(angle, pwm):
    duty_cycle = (angle/90) + 1.5
    pwm.ChangeDutyCycle(duty_cycle)


try:
    while True:
        set_angle(45, pwm1)
        set_angle(45, pwm2)
        sleep(0.5)
        pwm1.ChangeDutyCycle(0)
        pwm2.ChangeDutyCycle(0)
        sleep(0.5)
        set_angle(90, pwm1)
        set_angle(90, pwm2)
        sleep(0.5)
        pwm1.ChangeDutyCycle(0)
        pwm2.ChangeDutyCycle(0)



except KeyboardInterrupt:
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()

