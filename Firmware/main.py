import time
import struct
import cv2
import numpy as np
import serial
from rpi_hardware_pwm import HardwarePWM
from gpiozero import PWMOutputDevice, DigitalOutputDevice

OPENMV_PORT, OPENMV_BAUD = "/dev/ttyACM0", 115200
PWM_CHIP, PWM_CHANNEL, PWM_FREQ_HZ = 0, 2, 50
PULSE_CENTER = 1600
MOTOR_PWM_PIN, MOTOR_DIR_PIN, MOTOR_SLP_PIN = 12, 23, 24
MOTOR_SPEED = 0.40
MIN_PX = 350   

def lab_to_cv(t):
    Lmin, Lmax, Amin, Amax, Bmin, Bmax = t
    lo = np.array([int(Lmin * 2.55), Amin + 128, Bmin + 128], dtype=np.uint8)
    hi = np.array([int(Lmax * 2.55), Amax + 128, Bmax + 128], dtype=np.uint8)
    return lo, hi

THRESH_RED   = lab_to_cv((45, 55,  20,  38,   0, 20))
THRESH_GREEN = lab_to_cv((30, 42, -32, -18,   5, 20))

ser = serial.Serial(OPENMV_PORT, OPENMV_BAUD, timeout=2)
time.sleep(0.5)
ser.reset_input_buffer()

servo = HardwarePWM(pwm_channel=PWM_CHANNEL, hz=PWM_FREQ_HZ, chip=PWM_CHIP)
servo.start((PULSE_CENTER / 20000) * 100)  

motor_pwm = PWMOutputDevice(MOTOR_PWM_PIN, frequency=1000, initial_value=0)
motor_dir = DigitalOutputDevice(MOTOR_DIR_PIN, initial_value=False)
motor_slp = DigitalOutputDevice(MOTOR_SLP_PIN, initial_value=True)   # aufwecken
time.sleep(0.1)


def grab_frame():
    ser.write(b"snap")
    length_bytes = ser.read(4)
    if len(length_bytes) != 4:
        return None
    length = struct.unpack("<L", length_bytes)[0]
    if length == 0 or length > 200_000:
        ser.reset_input_buffer()
        return None
    jpeg = ser.read(length)
    if len(jpeg) != length:
        return None
    return cv2.imdecode(np.frombuffer(jpeg, np.uint8), cv2.IMREAD_COLOR)


def has_color(lab_img, thresh):
    mask = cv2.inRange(lab_img, thresh[0], thresh[1])
    return int(cv2.countNonZero(mask)) >= MIN_PX


def forward():
    motor_dir.off()
    motor_pwm.value = MOTOR_SPEED


def backward():
    motor_dir.on()
    motor_pwm.value = MOTOR_SPEED


def stop():
    motor_pwm.value = 0
  
try:
    while True:
        frame = grab_frame()
        if frame is None:
            time.sleep(0.05)
            continue

        lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
        green = has_color(lab, THRESH_GREEN)
        red   = has_color(lab, THRESH_RED)

        if green:
            forward()
        elif red:
            backward()
        else:
            stop()
            print("--    -> STOP")

        time.sleep(0.05)

except KeyboardInterrupt:
    print("Cancel")

finally:
    motor_pwm.value = 0
    motor_slp.off()
    servo.change_duty_cycle((PULSE_CENTER / 20000) * 100)
    time.sleep(0.2)
    servo.stop()
    ser.close()
