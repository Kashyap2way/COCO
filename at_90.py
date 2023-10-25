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

FRS_servo.mid()
FLS_servo.mid()
BRS_servo.mid()
BLS_servo.mid()

FRE_servo.mid()
FLE_servo.mid()
BRE_servo.mid()
BLE_servo.mid()

sleep(2)

FRS_servo.max()
FLS_servo.max()
BRS_servo.max()
BLS_servo.max()

FRE_servo.max()
FLE_servo.max()
BRE_servo.max()
BLE_servo.max()

