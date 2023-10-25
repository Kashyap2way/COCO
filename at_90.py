from gpiozero import Servo
from time import sleep

def val(angle):
    v = (angle - 90)/90
    return v

FRS_pin = 9
FLS_pin = 4
BRS_pin = 27
BLS_pin = 11

FRE_pin = 6
FLE_pin = 25
BRE_pin = 13
BLE_pin = 17

FRS_servo = Servo(FRS_pin)
FLS_servo = Servo(FLS_pin)
BRS_servo = Servo(BRS_pin)
BLS_servo = Servo(BLS_pin)

FRE_servo = Servo(FRE_pin)
FLE_servo = Servo(FLE_pin)
BRE_servo = Servo(BRE_pin)
BLE_servo = Servo(BLE_pin)

FRS_servo.value = val(90)
FLS_servo.value = val(90)
BRS_servo.value = val(90)
BLS_servo.value = val(90)

FRE_servo.value = val(45)
FLE_servo.value = val(45)
BRE_servo.value = val(45)
BLE_servo.value = val(45)
