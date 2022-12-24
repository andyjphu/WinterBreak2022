from helpers import helpers
import math, pygame, factory, random, os, companion_art, market


times_manufactured = 0

companion_art_manager = companion_art.companion_art()
sawmill = factory.Factory("sawmill")



while True:
    os.system("Clear")
    sawmill.raw_stock += random.randint(-1,3)
    
    if sawmill.manufactured_stock>0:
        buy_order_quantity = (int(sawmill.manufactured_stock * random.choice([1, 0.5, 0.25, 0.25, 0.1, 0.1,0,0,0, 0,0,0,0])))
        sawmill.manufactured_stock-= buy_order_quantity
        sawmill.capital += buy_order_quantity
    
    print(sawmill)
    if sawmill.manufacture():
        
        companion_art_manager.print_active_factory()
        companion_art_manager.print_boxes(int(sawmill.manufactured_stock //1 ))
        print(f"𓆭 -> ⧅ : {helpers.truncate(sawmill.throughput_efficiency)}") 
    else:
        
        companion_art_manager.print_inactive_factory()
        companion_art_manager.print_boxes(int(sawmill.manufactured_stock // 1))
        print(f"unsuccessful manufacture attempt, not enough raw resources")
    
    if "exit" in input("[ENTER] to manufacture, 'm' to visit the market: "):
        exit()



#Ctrl C to trigger mac keyboardinterrupt (unix?)