from factory import *
from helpers import helpers
import math, pygame, random, os


with open("ascii_art/active_factory.txt") as active_factory_file:
    active_factory_image = "".join(active_factory_file.readlines())
with open("ascii_art/active_factory1.txt") as active_factory1_file:
    active_factory1_image = "".join(active_factory1_file.readlines())
with open("ascii_art/inactive_factory.txt") as inactive_factory_image:
    inactive_factory_image = "".join(inactive_factory_image.readlines())

times_manufactured = 0


sawmill = Factory("sawmill")
#initialization stuff


while True:
    os.system("Clear")
    sawmill.raw_stock += random.randint(-1,3)
    
    print(sawmill)
    if sawmill.manufacture():
        times_manufactured += 1
        if times_manufactured % 2:
            print(active_factory1_image)
        else:
            print(active_factory_image)
        print(f"successful manufacture, raw stock is now {helpers.truncate(sawmill.raw_stock)}, and manufactured stock is at {helpers.truncate(sawmill.manufactured_stock)}")
    else:
        print(inactive_factory_image)
        print(f"unsuccessful manufacture attempt, not enough raw resources")
    
    if "exit" in input("type anything to continue: "):
        exit()
        #os.system("exit()")
    



#both forms need to be completed, one customs form per family and need to have passport and writing tool for both-- yellow form needs to be completed regardless of passing through (aswith the customs form)
#I WAS LIED TO

#Ctrl C to trigger mac keyboardinterrupt (unix?)