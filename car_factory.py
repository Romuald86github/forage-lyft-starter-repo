from calliope import Calliope
from glissade import Glissade  # Import other car models...

class CarFactory:
    def create_car(self, model, last_service_date):
        if model == "Calliope":
            return Calliope(last_service_date)
        elif model == "Glissade":
            return Glissade(last_service_date)
        # Add other car models...
        else:
            raise ValueError("Invalid car model")

