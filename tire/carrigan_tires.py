from abc import ABC
from tire.model.tire import Tires

class CarriganTires(Tires, ABC):
    def __init__(self, Tire_Read):
        self.current_Tire_Status = Tire_Read

    def tire_should_be_serviced(self):
        for i in self.current_Tire_Status:
            if i >= 0.9:
                return True
            
        return False
