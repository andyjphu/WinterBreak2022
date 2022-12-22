from helpers import helpers

class Factory():
    def __init__(self, name):
        self.name = name
        self.raw_stock = 0
        self.manufactured_stock = 0
        self.capital = 0 
        self.base_throughput_efficiency = 1
        self.throughput_efficiency = self.base_throughput_efficiency / (self.manufactured_stock+1)
    
    def __repr__(self):
        raw_stockf = helpers.truncate(self.raw_stock)
        manufactured_stockf = helpers.truncate(self.manufactured_stock)
        throughput_efficiencyf = helpers.truncate(self.throughput_efficiency*100,3)
        return f"RS: {raw_stockf}    MS: {manufactured_stockf}     $: {self.capital}    EF: {throughput_efficiencyf}%"
        
    def manufacture(self):
        self.throughput_efficiency = self.base_throughput_efficiency / (self.manufactured_stock+1)
        
        if self.raw_stock > 0:
            self.raw_stock -= 1 * self.throughput_efficiency
            self.manufactured_stock += 1 * self.throughput_efficiency
            
            return True             
        else:
            return False 
    
    
    