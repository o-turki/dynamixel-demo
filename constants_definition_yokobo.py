"""
    - Dynamixel Constants
    Author: Othman Turki
    Date: 2022/11/01
"""

# Control table address
ADDR_MX_TORQUE_ENABLE = 64
ADDR_MX_GOAL_POSITION = 116
ADDR_MX_PRESENT_POSITION = 132
ADDR_PRO_GOAL_VEL = 104
ADDR_PRO_PRESENT_VEL = 128
ADDR_PRO_OPERATING_MODE = 11

# Protocol version
PROTOCOL_VERSION = 2.0

# Default settings
DXL1_ID = 11  # base motor
DXL2_ID = 12  # mid motor
DXL3_ID = 13  # top motor

BAUDRATE = 57600
DEVICENAME = 'COM13'  # '/dev/ttyUSB0'

TORQUE_ENABLE = 1  # Value for enabling the torque
TORQUE_DISABLE = 0  # Value for disabling the torque

# MOTOR LIMITS
MOTOR_1_CENTER = 2015  # base motor
MOTOR_2_CENTER = 2010  # 1800
MOTOR_3_CENTER = 3000
MOTOR_1_MIN_LIM = MOTOR_1_CENTER - 600  # 1415
MOTOR_1_MAX_LIM = MOTOR_1_CENTER + 600  # 2615
MOTOR_2_MIN_LIM = MOTOR_2_CENTER - 350  # 1660
MOTOR_2_MAX_LIM = MOTOR_2_CENTER + 350  # 2360
MOTOR_3_MIN_LIM = MOTOR_3_CENTER - 900  # 2100
MOTOR_3_MAX_LIM = MOTOR_3_CENTER + 900  # 3900
