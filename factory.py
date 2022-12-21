class Factory():
    def __init__(self, name):
        self.name = name
        self.raw_stock = 0
        self.manufactured_stock = 0
    
    def __repr__(self):
        return f"{self.name} has {self.raw_stock} units of raw stock and {self.manufactured_stock} units of manufactured stock"
        
    def manufacture(self):
        if self.raw_stock > 0:
            self.raw_stock -= 1
            self.manufactured_stock += 1
            
            return True             
        else:
            return False 
    
    
    