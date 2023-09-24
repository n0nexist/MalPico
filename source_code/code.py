"""
MalPico - github.com/n0nexist/MalPico
BadUSB firmware for the raspberry pico W
"""

# default imports
import board
import digitalio
import time
import usb_hid

# external imports
from lib.adafruit_hid.keyboard import Keyboard
from lib.adafruit_hid.keycode import Keycode
from lib.adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from lib.adafruit_hid.mouse import Mouse

# import the payload
from payload import run

# setup default led
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# setup keyboard and mouse
KEYBOARD = Keyboard(usb_hid.devices)
LAYOUT = KeyboardLayoutUS(KEYBOARD)
MOUSE = Mouse(usb_hid.devices)

# tells the user that the script started
led.value = True
time.sleep(0.5)

# starts the payload
run(KEYBOARD,LAYOUT,Keycode,MOUSE,time)

# tells the user the script is finished
while True:
    time.sleep(0.1)
    led.value = not led.value