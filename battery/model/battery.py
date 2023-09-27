from abc import ABC, abstractmethod

class Battery(ABC):
    def __init__(self, passed_battery, passed_engine):
        self.CarBattery = passed_battery
        self.CarEngine = passed_engine

    @abstractmethod
    def needs_service(self):
        pass
