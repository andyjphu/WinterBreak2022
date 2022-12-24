class companion_art:

    def __init__(self) -> None:
        self.image_dictionary = {}     
        with open("ascii_art/A1.txt") as A1_F:
            self.image_dictionary["A1"] = "".join(A1_F.readlines())
        with open("ascii_art/A2.txt") as A2_F:
            self.image_dictionary["A2"] = "".join(A2_F.readlines())
        with open("ascii_art/A3.txt") as A3_F:
            self.image_dictionary["A3"] = "".join(A3_F.readlines())
        with open("ascii_art/I.txt") as I1_F:
            self.image_dictionary["I"] = "".join(I1_F.readlines())
            
        self.cycled = -1
        
    def print_active_factory(self):
        '''
            Purpose:
                lmao does cycle thing doge
            Param:
            Return:
        '''
        self.cycled += 1
        print(self.image_dictionary[f"A{(self.cycled % 3) + 1}"])
    
    def print_inactive_factory(self):
        print(self.image_dictionary["I"])
    
    def print_boxes(self, num):
        print()
        print()
        
        
        print("".join(["⧅" for i in range(num)]))
        print()