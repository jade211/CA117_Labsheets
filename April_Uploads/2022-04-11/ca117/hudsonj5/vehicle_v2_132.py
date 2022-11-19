#!/usr/bin/env python3

class Vehicle(object):

    def __init__(self, id, category, mileage, drivers=None):
        self.vin = id
        self.cat = category
        self.mileage = mileage
        if drivers is None:
            self.drivers = []
        else:
            self.drivers = drivers

    def add_driver(self, driver):
        if driver not in self.drivers:
            self.drivers.append(driver)

    def __str__(self):
        info = []
        info.append(f"ID: {self.vin}")
        info.append(f"Category: {self.cat}")
        info.append(f"Mileage: {self.mileage}")
        info.append(f"Drivers: {', '.join(self.drivers)}")
        return "\n".join(info)
