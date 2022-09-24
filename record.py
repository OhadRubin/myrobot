#!/usr/bin/env python

"""
This package need `pymycobot`.
This file for test the API if right.
Just can run in Linux.
"""

import time, random, subprocess
from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle, Coord
import json

import click
@click.group()
def cli():
    pass

@cli.command()
@click.argument("file_name")
@click.option("--offset",default=0)
@click.option("--lookback",default=None)
def run_json(file_name,offset,lookback):
    mycobot = MyCobot("/dev/ttyTHS1",1000000)
    with  open(file_name) as f:
        angle_list = json.load(f)[offset:]
    while True:
        for i,coords in enumerate(angle_list):
            print(i+offset,coords)
            mycobot.send_angles(coords, 85)
            time.sleep(0.10)
@cli.command()
@click.argument("file_name")
def record_json(file_name):
    mycobot = MyCobot("/dev/ttyTHS1",1000000)
    print(f"Recording to {file_name}")
    angle_list = []
    try:
        while True:
        # for i in range(500):
            degrees = mycobot.get_angles()
            print(degrees)
            angle_list.append(degrees)
            time.sleep(0.1)
    except KeyboardInterrupt:
        with open(file_name,"w") as f:
            json.dump(angle_list,f)
if __name__ == '__main__':
    cli()
# if __name__ == "__main__":
#     args = parser.parse_args()
    
#     # file_name
#     # run_json(mycobot)
#     record_json("good_action.json",mycobot)
#     # print("Start recording\n")

    