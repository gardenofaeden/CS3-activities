from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_reading():
        pass


class TempSensor(Sensor):
    def get_reading(self):
        return "[pH Sensor] Reading: 24.5°C"

class PHSensor(Sensor):
    def get_reading(self):
        return "[Temperature Sensor] Reading: 7.2 pH (Neutral)"

sensor1 = TempSensor()
sensor2 = PHSensor()
print("--- Lab Inventory System ---")
print(sensor1.get_reading())
print(sensor2.get_reading())
print("\n----------------------------")

