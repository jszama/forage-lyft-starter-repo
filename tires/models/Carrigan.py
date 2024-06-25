from tires.Tire import Tire

class Carrigan(Tire):    
    def needs_service(self):
        return sum(self.wear) >= 0.9
