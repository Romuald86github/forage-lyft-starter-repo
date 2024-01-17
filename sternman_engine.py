from engine import Engine

class SternmanEngine(Engine):
    def service_interval(self):
        return None  # Service only when the warning indicator is on

