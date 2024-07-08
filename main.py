from utime import sleep
from hx711 import HX711

hx711 = HX711(19, 18, 1)

print('..')

def read_weight(sensor):
    """Reads and prints the weight from the HX711 sensor."""
    sensor.power_on()
    
    while sensor.is_ready():
        pass
    
    raw_measurement = sensor.read(False)
    print(raw_measurement)
    
    while sensor.is_ready():
        pass
    
    raw_measurement = sensor.read(True)
    print(raw_measurement)
    
    weight = raw_measurement / 420
    print('Total Weight is:', weight)

while True:
    read_weight(hx711)
    sleep(1)
