# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple demo of the MAX31865 thermocouple amplifier.
# Will print the temperature every second.
import time
import board
import busio
import digitalio
import constants_old
import numpy as np

import adafruit_max31865

# Initialize SPI bus and sensor.
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs1 = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.
cs2 = digitalio.DigitalInOut(board.D6)  # Chip select of the MAX31865 board.


#sensor = adafruit_max31865.MAX31865(spi, cs)
# Note you can optionally provide the thermocouple RTD nominal, the reference
# resistance, and the number of wires for the sensor (2 the default, 3, or 4)
# with keyword args:
sensor = adafruit_max31865.MAX31865(spi, cs1, rtd_nominal=1000, ref_resistor=4300.0, wires=3)
sensor2 = adafruit_max31865.MAX31865(spi, cs2, rtd_nominal=1000, ref_resistor=4300.0, wires=3)


# Main loop to print the temperature every second.
def collect_temp():
    while True:
        # Read temperature.
        temp1 = sensor.temperature
        temp2 = sensor2.temperature
        if ((temp1 > 200) | (temp2 > 200)):
            # Print the value
            print(np.nan)
        
        else:
            print("Steam Temp: {0:0.2f}C".format(temp1))
            print("Surrounding Temp: {0:0.2f}C".format(temp2))
        # Delay for a second.
        time.sleep(1.0)
        
collect_temp()