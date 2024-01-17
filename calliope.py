from car import Car
from capulet_engine import CapuletEngine
from spindler_battery import SpindlerBattery

class Calliope(Car):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)
        self.engine = CapuletEngine()
        self.battery = SpindlerBattery()

    def needs_service(self):
        # Implement service logic based on last service date and service 
intervals
        pass

