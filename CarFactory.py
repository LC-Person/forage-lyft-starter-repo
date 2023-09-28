from abc import ABC, abstractmethod
from car import Car

#engines
from engine import capulet_engine, sternman_engine, willoughby_engine
#car model
from battery import nubbin, spindler

class CarFactory():
    def create_calliope(current_date, last_service_date, current_milage, last_service_milage):
        usingEngine = capulet_engine.CapuletEngine(current_mileage=current_milage, last_service_mileage=last_service_milage)
        usingBattery = spindler.SpindlerBattery(last_service_date=last_service_date)
        
        Assembled_Car = Car(passed_battery=usingBattery, passed_engine=usingEngine)
        
        return Assembled_Car
    
    def create_glissade(current_date, last_service_date, current_milage, last_service_milage):
        usingEngine = willoughby_engine.WilloughbyEngine(current_mileage=current_milage,last_service_mileage=last_service_milage)
        usingBattery = spindler.SpindlerBattery(last_service_date=last_service_date)

        Assembled_Car = Car(passed_battery=usingBattery, passed_engine=usingEngine)
        
        return Assembled_Car
    
    def create_palindrome(current_date, last_service_date, warning_light_on):
        usingEngine = sternman_engine.SternmanEngine(warning_light_is_on=warning_light_on)
        usingBattery = nubbin.NubbinBattery(last_service_date=last_service_date)
        
        Assembled_Car = Car(passed_battery=usingBattery, passed_engine=usingEngine)
        
        return Assembled_Car
    
    def create_rorschach(current_date, last_service_date, current_milage, last_service_milage):
        usingEngine = willoughby_engine.WilloughbyEngine(current_mileage=current_milage, last_service_mileage=last_service_milage)
        usingBattery = nubbin.NubbinBattery(last_service_date=last_service_date)
        
        Assembled_Car = Car(passed_battery=usingBattery, passed_engine=usingEngine)
        
        return Assembled_Car
    
    def create_thovex(current_date, last_service_date, current_milage, last_service_milage):
        usingEngine = capulet_engine.CapuletEngine(current_mileage=current_milage, last_service_mileage=last_service_milage)
        usingBattery = nubbin.NubbinBattery(last_service_date=last_service_date)

        Assembled_Car = Car(passed_battery=usingBattery, passed_engine=usingEngine)

        return Assembled_Car