import smbus
import math
import time

# MPU6050 Registers and addresses
DEVICE_ADDRESS = 0x68  # MPU6050 device address
PWR_MGMT_1 = 0x6B  # Power Management 1 register
ACCEL_XOUT = 0x3B  # Accelerometer data registers

# MPU6050 scale factor for converting raw values to degrees
ACCEL_SCALE_FACTOR = 16384.0  # Corresponds to ±2g sensitivity

# Robot leg distances
front_back_leg_distance = 320  # mm
side_leg_distance = 150  # mm

# PID constants
kp = 0.5  # Proportional constant
ki = 0.1  # Integral constant
kd = 0.1  # Derivative constant

# Target angles to maintain balance
target_x_angle = 0  # Adjust as needed
target_y_angle = 0  # Adjust as needed

# PID variables
last_error_x = 0
last_error_y = 0
integral_x = 0
integral_y = 0

# Create a smbus object
bus = smbus.SMBus(1)  # For revision 2 boards (512MB)

# Function to read raw sensor data
def read_raw_data(addr):
    high = bus.read_byte_data(DEVICE_ADDRESS, addr)
    low = bus.read_byte_data(DEVICE_ADDRESS, addr + 1)
    value = (high << 8) | low
    if value > 32767:
        value -= 65536
    return value

# Initialize MPU6050
bus.write_byte_data(DEVICE_ADDRESS, PWR_MGMT_1, 0)

# Function to calculate PID output
def calculate_pid_output(error, last_error, integral, kp, ki, kd):
    integral = integral + error
    derivative = error - last_error
    output = (kp * error) + (ki * integral) + (kd * derivative)
    return output, integral

# Function to check if the error is within the margin
def within_margin(error):
    return abs(error) > 2

# Robot leg distance from the ground
leg_distance_from_ground = 170  # mm

try:
    while True:
        # Read raw accelerometer data
        raw_x = read_raw_data(ACCEL_XOUT)
        raw_y = read_raw_data(ACCEL_XOUT + 2)

        # Calculate angles
        x_angle = math.atan2(raw_y, math.sqrt(raw_x * raw_x + raw_y * raw_y)) * (180 / math.pi)
        y_angle = math.atan2(-raw_x, math.sqrt(raw_x * raw_x + raw_y * raw_y)) * (180 / math.pi)

        # Compute errors
        error_x = target_x_angle - x_angle
        error_y = target_y_angle - y_angle

        # Check if errors are within the margin
        if not (within_margin(error_x) or within_margin(error_y)):
            time.sleep(0.1)  # Wait and continue loop
            continue

        # Calculate PID outputs for X and Y axes
        output_x, integral_x = calculate_pid_output(error_x, last_error_x, integral_x, kp, ki, kd)
        output_y, integral_y = calculate_pid_output(error_y, last_error_y, integral_y, kp, ki, kd)

        # Update last errors
        last_error_x = error_x
        last_error_y = error_y

        # Calculate adjustments for leg lengths based on PID output
        front_leg_adjustment = output_y * (front_back_leg_distance / 2)
        back_leg_adjustment = -output_y * (front_back_leg_distance / 2)
        side_leg_adjustment = output_x * (side_leg_distance / 2)

        # Calculate adjustments for leg heights from the ground
        front_leg_height_adjustment = output_y * (leg_distance_from_ground / 2)
        back_leg_height_adjustment = -output_y * (leg_distance_from_ground / 2)
        side_leg_height_adjustment = output_x * (leg_distance_from_ground / 2)

        # Apply adjustments to leg lengths and heights from the ground
        # Implement logic to control the robot's legs based on adjustments calculated

        time.sleep(0.1)  # Adjust sleep time as needed

except KeyboardInterrupt:
    pass

