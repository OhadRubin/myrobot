
# python3 -m pip install evdev
# cat /proc/bus/input/devices
import time, random, subprocess
from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle, Coord
import json
import numpy as np 


from evdev import InputDevice, categorize, ecodes
gamepad = InputDevice("/dev/input/event6")



mycobot = MyCobot("/dev/ttyTHS1",1000000)
mycobot.send_angles([0,0,0,0,0,0],50)

time.sleep(2)

LEFT_SIDE,RIGHT_SIDE = 0,1
UP_DOWN, LEFT_RIGHT = 0,1
SIDE = {0:LEFT_SIDE,1:LEFT_SIDE,2:RIGHT_SIDE,5:RIGHT_SIDE}
AXIS = {0:LEFT_RIGHT,2:LEFT_RIGHT,1:UP_DOWN,5:UP_DOWN}
def get_real_value(value):
    if abs(value-128)>9:
        return value-128
    else:
        return 0
original_state = np.array(mycobot.get_angles())
current_state = np.zeros([3,2],dtype=np.float32)

beta = 0.0
momentum = np.zeros([3,2],dtype=np.float32)
counter = 0

# for event in gamepad.read_loop():

    

if False:
    for event in gamepad.read_loop():
        delta  = np.zeros([3,2],dtype=np.float32)
        if event is not None and event.type not in [0]:
            axis = AXIS[event.code]
            side = SIDE[event.code]
            val = get_real_value(event.value)
            delta[axis][side] += val
        momentum = beta*momentum+np.clip(delta,-1.5,1.5)
        momentum = np.clip(momentum,-1.5,1.5)
        current_state = current_state+ momentum
        current_state = np.clip(current_state,-255,255)
        if ( (counter%4) ==0):
            updated_state = original_state+current_state.flatten()
            mycobot.send_angles(list(updated_state),20)
        counter+=1
