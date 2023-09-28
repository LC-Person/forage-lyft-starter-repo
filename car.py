from abc import ABC, abstractmethod

class Car():
    def __init__(self, passed_battery, passed_engine, passed_tires):
        self.CarBattery = passed_battery
        self.CarEngine = passed_engine
        self.CarTires = passed_tires

    def needs_service(self):
        return ((self.CarEngine.engine_should_be_serviced() or self.CarBattery.battery_needs_service()) or self.CarTires.tire_should_be_serviced())
