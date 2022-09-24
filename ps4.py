
# python3 -m pip install evdev
# cat /proc/bus/input/devices
import time, random, subprocess
from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle, Coord
import json
import numpy as np 

from pyPS4Controller.controller import Controller

mycobot = MyCobot("/dev/ttyTHS1",1000000)
mycobot.send_angles([0,0,0,0,0,0],50)

time.sleep(2)

LEFT_SIDE,RIGHT_SIDE = 0,1
UP_DOWN, LEFT_RIGHT = 0,1
SIDE = {0:LEFT_SIDE,1:LEFT_SIDE,2:RIGHT_SIDE,5:RIGHT_SIDE}
AXIS = {0:LEFT_RIGHT,2:LEFT_RIGHT,1:UP_DOWN,5:UP_DOWN}
mycobot.set_fresh_mode(1)
class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        self.curr_state =[0,0,0,0,0]
    def update_curr_state(self):
        state = mycobot.get_angles()
        if len(state)>0:
            self.curr_state = np.array(state)

    def on_up_arrow_press(self):
        self.update_curr_state()
        # curr_state = np.array())
        # print(value)
        self.curr_state[0]+=20
        mycobot.send_angles(list(self.curr_state),90)
        # time.sleep(0.1)

    def on_down_arrow_press(self):
        self.update_curr_state()
        # print(value)
        self.curr_state[0]-=20
        mycobot.send_angles(list(self.curr_state),90)
        # time.sleep(0.1)

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60)