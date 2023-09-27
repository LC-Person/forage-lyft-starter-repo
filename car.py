from abc import ABC, abstractmethod

class Car():
    def __init__(self, passed_battery, passed_engine):
        self.CarBattery = passed_battery
        self.CarEngine = passed_engine

    def needs_service(self):
        return (self.CarEngine.engine_should_be_serviced() or self.CarBattery.battery_needs_service())
