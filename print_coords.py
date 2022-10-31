
from pymycobot.mycobot import MyCobot
mycobot = MyCobot("/dev/ttyTHS1",1000000)
while True:
    print(mycobot.get_coords())


