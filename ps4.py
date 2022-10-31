
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

PASS_LIST = ["on_x_press", "on_x_release", "on_triangle_press", "on_triangle_release", "on_circle_press", "on_circle_release", "on_square_press", "on_square_release",
"on_L1_press", "on_L1_release", "on_L2_press", "on_L2_release", "on_R1_press", "on_R1_release", "on_R2_press", "on_R2_release", "on_up_arrow_press",
"on_up_down_arrow_release", "on_down_arrow_press", "on_left_arrow_press", "on_left_right_arrow_release", "on_right_arrow_press", "on_L3_up", "on_L3_down",
"on_L3_left", "on_L3_right", "on_L3_y_at_rest", "on_L3_x_at_rest", "on_L3_press", "on_L3_release", "on_R3_up", "on_R3_down", "on_R3_left", "on_R3_right",
"on_R3_y_at_rest", "on_R3_x_at_rest", "on_R3_press", "on_R3_release", "on_options_press", "on_options_release",
"on_share_press", "on_share_release", "on_playstation_button_press", "on_playstation_button_release", "on_down_arrow_press"]

global state
state = np.zeros(6)
def pf(state):
    return state

e1 = np.array([1,0,0,0,0,0])
e2 = np.array([0,1,0,0,0,0])
e3 = np.array([0,0,1,0,0,0])
e4 = np.array([0,0,0,1,0,0])
e5 = np.array([0,0,0,0,1,0])
e6 = np.array([0,0,0,0,0,1])

def add(y):
    move_func = lambda x: x+y
    return move_func

func_dict = {"on_x_press":pf, "on_x_release":pf, "on_triangle_press":pf, "on_triangle_release":pf, "on_circle_press":pf, "on_circle_release":pf, "on_square_press":pf, "on_square_release":pf,
"on_L1_press":pf, "on_L1_release":pf, "on_L2_press":pf, "on_L2_release":pf, 
"on_R1_press":pf, "on_R1_release":pf, "on_R2_press":pf, "on_R2_release":pf,
"on_up_arrow_press":add(-e2),"on_down_arrow_press":add(e2),
"on_up_down_arrow_release":pf,
"on_left_right_arrow_release":pf,
"on_right_arrow_press":add(-e1), "on_left_arrow_press":add(e1),
"on_L3_up":pf, "on_L3_down":pf,
"on_L3_left":pf, "on_L3_right":pf, "on_L3_y_at_rest":pf, "on_L3_x_at_rest":pf, "on_L3_press":pf, "on_L3_release":pf, "on_R3_up":pf, "on_R3_down":pf, "on_R3_left":pf, "on_R3_right":pf,
"on_R3_y_at_rest":pf, "on_R3_x_at_rest":pf, "on_R3_press":pf, "on_R3_release":pf, "on_options_press":pf, "on_options_release":pf,
"on_share_press":pf, "on_share_release":pf, "on_playstation_button_press":pf, "on_playstation_button_release":pf,
#  "on_up_arrow_press":pf,
  }

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
    
import numpy as np

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
def get_f(x):
    
    def f(*args):
        global state
        state = func_dict[x](state)
        mycobot.send_angles(list(4*state),50)

        print(f"{x}: {state}")
        
    return f
for x in PASS_LIST:
    setattr(controller,x,get_f(x)) 
# controller.debug = True 
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen()
while True:
    print("hi")