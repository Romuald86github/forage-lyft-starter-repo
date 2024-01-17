from abc import ABC, abstractmethod

class ServiceStrategy(ABC):
    @abstractmethod
    def calculate_service_interval(self, car):
        pass

