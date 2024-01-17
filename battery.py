from abc import ABC, abstractmethod

class Battery(ABC):
    @abstractmethod
    def service_interval(self):
        pass

