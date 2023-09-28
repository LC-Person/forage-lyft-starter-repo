from abc import ABC
from tire.model.tire import Tires

class OctoprimeTires(Tires, ABC):
    def __init__(self, Tire_Read):
        self.current_Tire_Status = Tire_Read

    def tire_should_be_serviced(self):
        sum = 0

        for i in self.current_Tire_Status:
            sum = sum + i
            
        return (sum >= 3)
