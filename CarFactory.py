from abc import ABC, abstractmethod
from car import Car

#Engines
from engine import capulet_engine, sternman_engine, willoughby_engine
#Batteries
from battery import nubbin, spindler
#Tires
from tire import carrigan_tires, octoprime_tires

class CarFactory():
    def create_calliope(Tire_Health, current_date, last_service_date, current_milage, last_service_milage):
        usingEngine = capulet_engine.CapuletEngine(current_mileage=current_milage, last_service_mileage=last_service_milage)
        usingBattery = spindler.SpindlerBattery(last_service_date=last_service_date)
        usingTires = carrigan_tires.CarriganTires(Tire_Read=Tire_Health)

        Assembled_Car = Car(passed_battery=usingBattery, passed_engine=usingEngine, passed_tires=usingTires)
        
        return Assembled_Car
    
    def create_glissade(Tire_Health, current_date, last_service_date, current_milage, last_service_milage):
        usingEngine = willoughby_engine.WilloughbyEngine(current_mileage=current_milage,last_service_mileage=last_service_milage)
        usingBattery = spindler.SpindlerBattery(last_service_date=last_service_date)
        usingTires = carrigan_tires.CarriganTires(Tire_Read=Tire_Health)

        Assembled_Car = Car(passed_battery=usingBattery, passed_engine=usingEngine, passed_tires=usingTires)
        
        return Assembled_Car
    
    def create_palindrome(Tire_Health, current_date, last_service_date, warning_light_on):
        usingEngine = sternman_engine.SternmanEngine(warning_light_is_on=warning_light_on)
        usingBattery = nubbin.NubbinBattery(last_service_date=last_service_date)
        usingTires = carrigan_tires.CarriganTires(Tire_Read=Tire_Health)

        Assembled_Car = Car(passed_battery=usingBattery, passed_engine=usingEngine, passed_tires=usingTires)
        
        return Assembled_Car
    
    def create_rorschach(Tire_Health, current_date, last_service_date, current_milage, last_service_milage):
        usingEngine = willoughby_engine.WilloughbyEngine(current_mileage=current_milage, last_service_mileage=last_service_milage)
        usingBattery = nubbin.NubbinBattery(last_service_date=last_service_date)
        usingTires = octoprime_tires.OctoprimeTires(Tire_Read=Tire_Health)

        Assembled_Car = Car(passed_battery=usingBattery, passed_engine=usingEngine, passed_tires=usingTires)
        
        return Assembled_Car
    
    def create_thovex(Tire_Health, current_date, last_service_date, current_milage, last_service_milage):
        usingEngine = capulet_engine.CapuletEngine(current_mileage=current_milage, last_service_mileage=last_service_milage)
        usingBattery = nubbin.NubbinBattery(last_service_date=last_service_date)
        usingTires = octoprime_tires.OctoprimeTires(Tire_Read=Tire_Health)

        Assembled_Car = Car(passed_battery=usingBattery, passed_engine=usingEngine, passed_tires=usingTires)

        return Assembled_Car