from Car import Car
from engine.models import models
from battery.models import models as battery_models

class CarFactory:
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car( models.CapuletEngine(last_service_mileage, current_mileage), battery_models.SpindlerBattery(last_service_date, current_date))
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car( models.WilloughbyEngine(last_service_mileage, current_mileage), battery_models.SpindlerBattery(last_service_date, current_date))
    
    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        return Car( models.SternmanEngine(warning_light_on), battery_models.SpindlerBattery(last_service_date, current_date))
    
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car( models.WilloughbyEngine(last_service_mileage, current_mileage), battery_models.NubbinBattery(last_service_date, current_date))
    
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car( models.CapuletEngine(last_service_mileage, current_mileage), battery_models.NubbinBattery(last_service_date, current_date))