from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def service_interval(self):
        pass

