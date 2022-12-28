from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight = 0
    fuel = 0
    started = False
    fuel_consumption = 0

    def __init__(self, weight,  fuel, fuel_consumption ):
        self.weight = weight
        self.fuel_consumption = fuel_consumption
        self.fuel = fuel

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError()

    def move(self, path_length:int):
        if self.fuel - (self.fuel_consumption * path_length) >= 0:
            self.fuel -= (path_length * self.fuel_consumption)
        else:
            raise NotEnoughFuel()






