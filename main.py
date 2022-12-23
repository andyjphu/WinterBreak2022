from factory import *
from helpers import helpers
import math, pygame, random, os


with open("ascii_art/A1.txt") as active_factory_file:
    active_factory_image_1 = "".join(active_factory_file.readlines())
with open("ascii_art/A2.txt") as active_factory1_file:
    active_factory_image_2 = "".join(active_factory1_file.readlines())
with open("ascii_art/A3.txt") as active_factory1_file:
    active_factory_image_3 = "".join(active_factory1_file.readlines())
with open("ascii_art/I.txt") as inactive_factory_image:
    inactive_factory_image = "".join(inactive_factory_image.readlines())

times_manufactured = 0


sawmill = Factory("sawmill")



def spawn_buffer():
    print()
    for i in range(int(sawmill.manufactured_stock)):
        print("⧅",end="")
    print()
    print()

while True:
    os.system("Clear")
    sawmill.raw_stock += random.randint(-1,3)
    
    if sawmill.manufactured_stock>0:
        buy_order_quantity = (int(sawmill.manufactured_stock * random.choice([0.5, 0.25, 0.1, 0.1, 0,0,0,0])))
        sawmill.manufactured_stock-= buy_order_quantity
        sawmill.capital += buy_order_quantity
    
    print(sawmill)
    if sawmill.manufacture():
        times_manufactured += 1
        if times_manufactured % 3 ==0:
            print(active_factory_image_1)
        elif times_manufactured %3 == 1:
            print(active_factory_image_2)
        elif times_manufactured %3 == 2:
            print(active_factory_image_3)
            
        spawn_buffer()
        print(f"Δ: \n    𓆭 -> ⧅ : {helpers.truncate(sawmill.throughput_efficiency)}")
    else:
        print(inactive_factory_image)
        spawn_buffer()
        print(f"unsuccessful manufacture attempt, not enough raw resources")
    
    if "exit" in input("type anything to continue: "):
        exit()



#Ctrl C to trigger mac keyboardinterrupt (unix?)