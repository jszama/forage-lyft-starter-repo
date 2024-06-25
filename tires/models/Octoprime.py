from tires.Tire import Tire

class Octoprime(Tire):
    def needs_service(self):
        return sum(self.wear) >= 3