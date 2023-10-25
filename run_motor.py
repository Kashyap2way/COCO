from gpiozero import Servo
from time import sleep
import Stand_angle_adjust

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

stand = Stand_angle_adjust()
A1, A2 = stand.stand_adjust(0.124,0.135,0.2)
FRS_angle,  = A1

