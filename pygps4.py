import pygame
import json, os
# import os
# os.environ["SDL_VIDEODRIVER"] = "dummy"

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
# pygame.joystick.init()
for i in range(pygame.joystick.get_count()):
    joystick = pygame.joystick.Joystick(i)
    # print(joystick)
    joysticks.append(joystick)
for joystick in joysticks:
    joystick.init()

# for event in pygame.event.get():
with open(os.path.join("ps4_keys.json"), 'r+') as file:
    button_keys = json.load(file)
# 0: Left analog horizonal, 1: Left Analog Vertical, 2: Right Analog Horizontal
# 3: Right Analog Vertical 4: Left Trigger, 5: Right Trigger
analog_keys = {0:0, 1:0, 2:0, 3:0, 5:0}
import numpy as np
# START OF GAME LOOP
# state = np.array(mycobot.get_coords())

# if angle_mode:

def main():
    # mycobot.set_fresh_mode(1)
    angle_mode = True
    last_changed = time.time()
    time_since_state = time.time()
    def get_state():
        if angle_mode:
            return np.array(mycobot.get_angles())
        else:
            return np.array(mycobot.get_coords())
    # state = get_state()

    while running:
        for event in pygame.event.get():
            print(event)
            
            changed = False
            # time.sleep(0.01)
            # if event.type == pygame.JOYBUTTONUP or   event.type== pygame.JOYBUTTONDOWN:
                # angle_mode = not angle_mode

            # if angle_mode:
            #     #  or time_since_state-time.time() >0.001:
            #     state = get_state()
            #     # print(state,last_changed)
            #     while len(state)!=6:
            #         time.sleep(0.1)
            #         state = get_state()
                # break
            # delta = np.zeros(6)

            # if event.type == pygame.JOYHATMOTION:
            #     delta[:2] += np.array(event.value)
            #     changed =  sum(delta[:2]!=0)>0

                    
            # if event.type == pygame.JOYAXISMOTION:
            #     analog_keys[event.axis] = event.value
                
            #     if abs(analog_keys[0]) > .4:
            #         if  analog_keys[0] < -.7:
            #             delta[2] +=1 
            #             changed = True
            #         if  analog_keys[0] > .7:
            #             delta[2] -= 1
            #             changed = True
            #     if abs(analog_keys[1]) > .4:
            #         if  analog_keys[1] < -.7:
            #             delta[3] += 1
            #             changed = True
            #         if  analog_keys[1] > .7:
            #             delta[3] -=1
            #             changed = True
            #     if abs(analog_keys[2]) > .4:
            #         if  analog_keys[2] < -.7:
            #             delta[4] += 1
            #             changed = True
            #         if  analog_keys[2] > .7:
            #             delta[4] -= 1
            #             changed = True
            #         changed = True
            #     if abs(analog_keys[5]) > .4:
            #         if  analog_keys[5] < -.7:
            #             delta[5] += 1
            #             changed = True
            #         if  analog_keys[5] > .7:
            #             delta[5] -= 1
            #             changed = True
            #     del_rX, del_rY,del_X,del_Y,del_Z,del_rZ = delta
            #     delta = np.array([del_X,del_Y,del_Z,del_rX,del_rY,del_rZ])
            # print(delta)
            # time_since_cmd =  time.time()-last_changed
            # if angle_mode:
            #     movement_constant = 5
            #     state = np.clip(state,-160,160)
            #     if changed:
            #         state += movement_constant*delta
            #         # print(event)
            #         mycobot.send_angles(list(state),  80)
            # else:
            #     movement_constant = 2
                
            #     if changed:
            #         state += movement_constant*delta
            #         # print(event)
            #         mycobot.send_coords(list(state), 40,0)
            #         last_changed = time.time()
            # state = list(state)
                    # time.sleep(0.01)



        ################################# UPDATE WINDOW AND DISPLAY #################################
        # canvas.fill((255,255,255))
        # pygame.draw.rect(canvas, (0,0 + color,255), player)
        # window.blit(canvas, (0,0))
        # clock.tick(60)
        # pygame.display.update()


main()
# try:
# except Exception as e:
#     print(e)
#     mycobot.release_all_servos()
#     mycobot.send_angles([0,0,0,0,0,0],50)

# mycobot.release_all_servos()
# while True:

#     cors = mycobot.get_angles()
#     print(cors)