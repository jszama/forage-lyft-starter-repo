from Car import Car
from engine.models.CapuletEngine import CapuletEngine
from engine.models.SternmanEngine import SternmanEngine
from engine.models.WilloughbyEngine import WilloughbyEngine
from battery.models.SpindlerBattery import SpindlerBattery
from battery.models.NubbinBattery import NubbinBattery
from tires.models.Carrigan import Carrigan
from tires.models.Octoprime import Octoprime

class CarFactory:
    
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, wears):
        return Car(CapuletEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date), Carrigan(wears))
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, wears):
        return Car(WilloughbyEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date), Carrigan(wears))
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, wears):
        return Car(SternmanEngine(warning_light_on), SpindlerBattery(last_service_date, current_date), Octoprime(wears))
    
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, wears):
        return Car(WilloughbyEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date), Carrigan(wears))
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, wears):
        return Car(CapuletEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date), Octoprime(wears))
