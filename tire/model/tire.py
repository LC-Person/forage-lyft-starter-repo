from abc import ABC, abstractmethod

class Tires(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def tire_should_be_serviced(self):
        pass
