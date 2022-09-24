import pygame
import json, os

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

################################# LOAD UP A BASIC WINDOW #################################
pygame.init()
DISPLAY_W, DISPLAY_H = 960, 570
canvas = pygame.Surface((DISPLAY_W,DISPLAY_H))
window = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))
running = True
player = pygame.Rect(DISPLAY_W/2, DISPLAY_H/2, 60,60)
LEFT, RIGHT, UP, DOWN = False, False, False, False
clock = pygame.time.Clock()
color = 0
###########################################################################################

#Initialize controller
joysticks = []
for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
for joystick in joysticks:
    joystick.init()

with open(os.path.join("ps4_keys.json"), 'r+') as file:
    button_keys = json.load(file)
# 0: Left analog horizonal, 1: Left Analog Vertical, 2: Right Analog Horizontal
# 3: Right Analog Vertical 4: Left Trigger, 5: Right Trigger
analog_keys = {0:0, 1:0, 2:0, 3:0, 5:0}
import numpy as np
# START OF GAME LOOP
# state = np.array(mycobot.get_coords())
angle_mode = False
# if angle_mode:
mycobot.set_fresh_mode(1)
def get_state():
    if angle_mode:
        return np.array(mycobot.get_angles())
    else:
        return np.array(mycobot.get_coords())
def main():
    while running:
        for event in pygame.event.get():
            
            changed = False
            # time.sleep(0.01)
            
            
            state = get_state()
            print(state)
            while len(state)!=6:
                time.sleep(0.1)
                state = get_state()
                # break
            delta = np.zeros(6)

            if event.type == pygame.JOYHATMOTION:
                delta[:2] += np.array(event.value)
                changed =  sum(delta[:2]!=0)>0

                    
            if event.type == pygame.JOYAXISMOTION:
                analog_keys[event.axis] = event.value
                
                if abs(analog_keys[0]) > .4:
                    if  analog_keys[0] < -.7:
                        delta[2] += 1
                        changed = True
                    if  analog_keys[0] > .7:
                        delta[2] -= 1
                        changed = True
                if abs(analog_keys[1]) > .4:
                    if  analog_keys[1] < -.7:
                        delta[3] += 1
                        changed = True
                    if  analog_keys[1] > .7:
                        delta[3] -=1
                        changed = True
                if abs(analog_keys[2]) > .4:
                    if  analog_keys[2] < -.7:
                        delta[4] += 1
                        changed = True
                    if  analog_keys[2] > .7:
                        delta[4] -= 1
                        changed = True
                    changed = True
                if abs(analog_keys[5]) > .4:
                    if  analog_keys[5] < -.7:
                        delta[5] += 1
                        changed = True
                    if  analog_keys[5] > .7:
                        delta[5] -= 1
                        changed = True
                del_rX, del_rY,del_X,del_Y,del_Z,del_rZ = delta
                delta = np.array([del_X,del_Y,del_Z,del_rX,del_rY,del_rZ])
                                                                            
            if angle_mode:
                movement_constant = 10
                state = np.clip(state,-180,180)
                if changed:
                    state += movement_constant*delta
                    mycobot.send_angles(list(state), 60)
            else:
                movement_constant = 5
                
                if changed:
                    state += movement_constant*delta
                    # print(state)
                    mycobot.send_coords(list(state), 30,0)
                    # time.sleep(0.01)



        ################################# UPDATE WINDOW AND DISPLAY #################################
        # canvas.fill((255,255,255))
        # pygame.draw.rect(canvas, (0,0 + color,255), player)
        # window.blit(canvas, (0,0))
        # clock.tick(60)
        # pygame.display.update()


try:
    main()
except Exception as e:
    print(e)
    mycobot.release_all_servos()
    mycobot.send_angles([0,0,0,0,0,0],50)

# mycobot.release_all_servos()
# while True:

#     cors = mycobot.get_angles()
#     print(cors)