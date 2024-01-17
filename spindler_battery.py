from battery import Battery

class SpindlerBattery(Battery):
    def service_interval(self):
        return 2

