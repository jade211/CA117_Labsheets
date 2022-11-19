#!/usr/bin/env python3

class Vehicle(object):

    def __init__(self, id, category, mileage, drivers):
        self.vin = id
        self.cat = category
        self.mileage = mileage
        self.drivers = drivers

    def __str__(self):
        info = []
        info.append(f"ID: {self.vin}")
        info.append(f"Category: {self.cat}")
        info.append(f"Mileage: {self.mileage}")
        info.append(f"Drivers: {', '.join(self.drivers)}")
        return "\n".join(info)

class Fleet(object):

    def __init__(self):
        self.collection = {}

    def add(self, vehicle):
       self.collection[vehicle.vin] = vehicle

    def remove(self, id):
        if id in self.collection:
            del self.collection[id]

    def lookup(self, id):
        if id in self.collection:
            return self.collection[id]

    def get_drivers_by_category(self, vehicle_type):
        count = 0
        cars = []
        for v in self.collection.values():
            cars.append(v.cat)
        for car in cars:
            if car == vehicle_type:
                count = count + 1
        return count
