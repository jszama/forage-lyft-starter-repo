import unittest
from datetime import datetime
from car_factory.CarFactory import CarFactory

from battery.models.NubbinBattery import NubbinBattery
from battery.models.SpindlerBattery import SpindlerBattery
from engine.models.CapuletEngine import CapuletEngine
from engine.models.WilloughbyEngine import WilloughbyEngine
from engine.models.SternmanEngine import SternmanEngine
from tires.models.Carrigan import Carrigan
from tires.models.Octoprime import Octoprime

class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        wears = [0, 0, 0, 0]

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, wears)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        wears = [0, 0, 0, 0]

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, wears)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        wears = [0, 0, 0, 0]

        car = CarFactory.create_calliope(last_service_date, last_service_date, current_mileage, last_service_mileage, wears)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        wears = [0, 0, 0, 0]

        car = CarFactory.create_calliope(last_service_date, last_service_date, current_mileage, last_service_mileage, wears)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        wears = [0, 0, 0, 0]

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, wears)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        wears = [0, 0, 0, 0]

        car = CarFactory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, wears)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        wears = [0, 0, 0, 0]

        car = CarFactory.create_glissade(last_service_date, last_service_date, current_mileage, last_service_mileage, wears)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        wears = [0, 0, 0, 0]

        car = CarFactory.create_glissade(last_service_date, last_service_date, current_mileage, last_service_mileage, wears)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False
        wears = [0, 0, 0, 0]

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on, wears)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        warning_light_is_on = False
        wears = [0, 0, 0, 0]

        car = CarFactory.create_palindrome(today, last_service_date, warning_light_is_on, wears)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        wears = [0, 0, 0, 0]

        car = CarFactory.create_palindrome(last_service_date, last_service_date, warning_light_is_on, wears)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        wears = [0, 0, 0, 0]

        car = CarFactory.create_palindrome(last_service_date, last_service_date, warning_light_is_on, wears)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        wears = [0, 0, 0, 0]

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, wears)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        wears = [0, 0, 0, 0]

        car = CarFactory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, wears)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        wears = [0, 0, 0, 0]

        car = CarFactory.create_rorschach(last_service_date, last_service_date, current_mileage, last_service_mileage, wears)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        wears = [0, 0, 0, 0]

        car = CarFactory.create_rorschach(last_service_date, last_service_date, current_mileage, last_service_mileage, wears)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        wears = [0, 0, 0, 0]

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, wears)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        wears = [0, 0, 0, 0]

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, wears)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        wears = [0, 0, 0, 0]

        car = CarFactory.create_thovex(last_service_date, last_service_date, current_mileage, last_service_mileage, wears)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        wears = [0, 0, 0, 0]

        car = CarFactory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, wears)
        self.assertFalse(car.needs_service())


class TestBatteries(unittest.TestCase):
    def test_spindler_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery = SpindlerBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())
        
    def test_spindler_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        battery = SpindlerBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())
        
    def test_nubbin_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        battery = NubbinBattery(last_service_date, today)
        self.assertTrue(battery.needs_service())
        
    def test_nubbin_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        battery = NubbinBattery(last_service_date, today)
        self.assertFalse(battery.needs_service())
        
class TestEngines(unittest.TestCase):
    def test_capulet_engine_should_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 30001

        engine =  CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())
        
    def test_capulet_engine_should_not_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 30000

        engine =  CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())
        
    def test_willoughby_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        engine =  WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())
    
    def test_willoughby_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        engine =  WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())
        
    def test_sternman_engine_should_be_serviced(self):
        warning_light_is_on = True

        engine =  SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())
        
    def test_sternman_engine_should_not_be_serviced(self):
        warning_light_is_on = False

        engine =  SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())
        
class TestTires(unittest.TestCase):
    def test_carrigan_tires_should_be_serviced(self):
        wears = [2,3,6,4]

        tires =   Carrigan(wears)
        self.assertTrue(tires.needs_service())
        
    def test_carrigan_tires_should_not_be_serviced(self):
        wears = [0, 0, 0, 0]

        tires =   Carrigan(wears)
        self.assertFalse(tires.needs_service())
        
    def test_octoprime_tires_should_be_serviced(self):
        wears = [1, 2, 3, 4]

        tires =   Octoprime(wears)
        self.assertTrue(tires.needs_service())
        
    def test_octoprime_tires_should_not_be_serviced(self):
        wears = [0,1,1.5,0,0.2]

        tires =   Octoprime(wears)
        self.assertFalse(tires.needs_service())

if __name__ == '__main__':
    unittest.main()