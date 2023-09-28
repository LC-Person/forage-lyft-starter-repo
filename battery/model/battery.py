from abc import ABC, abstractmethod

class Battery(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def battery_needs_service(self):
        pass
