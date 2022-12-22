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
#initialization stuff




def spawn_random_buffer():
    print()
    for i in range(25):
        print(random.choice(["꠵꠵"," "]),end="")
        #['▖', '▗', '▘', '▙', '▚', '▛', '▜', '▝', '▞', '▟', '■']), end="")
        #['⬥','⬦','⬧','⬨','⬩','⬪','⬫']
        #"═","╬"
    print()

while True:
    os.system("Clear")
    sawmill.raw_stock += random.randint(-1,3)
    
    print(sawmill)
    if sawmill.manufacture():
        times_manufactured += 1
        if times_manufactured % 3 ==0:
            print(active_factory_image_1)
        elif times_manufactured %3 == 1:
            print(active_factory_image_2)
        elif times_manufactured %3 == 2:
            print(active_factory_image_3)
            
        spawn_random_buffer()
        print(f"𓆭 {helpers.truncate(sawmill.raw_stock)}, and manufactured stock is at {helpers.truncate(sawmill.manufactured_stock)}")
    else:
        print(inactive_factory_image)
        spawn_random_buffer()
        print(f"unsuccessful manufacture attempt, not enough raw resources")
    
    if "exit" in input("type anything to continue: "):
        exit()
        #os.system("exit()")
    



#both forms need to be completed, one customs form per family and need to have passport and writing tool for both-- yellow form needs to be completed regardless of passing through (aswith the customs form)
#I WAS LIED TO

#Ctrl C to trigger mac keyboardinterrupt (unix?)