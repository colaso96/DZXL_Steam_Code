import board
import busio
import digitalio
import adafruit_max31865

#------------------------------------------------------------------ CONSTANTS  ------------------------------------------------------------------
STEAM_SENSOR1 = 1
STEAM_SENSOR2 = 2
STEAM_SENSOR3 = 3
STEAM_SENSOR4 = 4 
STEAM_SENSOR5 = 5
STEAM_SENSOR6 = 6
TEMP_PROBE_STEAM = ''
TEMP_PROBE_SURR = ''
THRESHOLD = 12
TIME_INTERVAL = .5
START_PATH = ''
RTD_SPI = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
CS1 = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board
CS2 = digitalio.DigitalInOut(board.D6)  # Chip select of the MAX31865 board

#------------------------------------------------------------------ VARIABLES  ------------------------------------------------------------------
df = ''
START_TIME = 0
UPDATED_TIME = -1
ADDITIONAL_MINS = -1
TEMP_PROBE_STATE = True

#------------------------------------------------------------------ INPUTS ------------------------------------------------------------------
STEAM_APPLIANCE = ''
FUNCTION = ''
FOOD_LOAD = ''
MONITOR_TIME = -1
SENSOR_HEIGHT = 0
INITIAL_WATER_MASS = 0
FINAL_WATER_MASS = 0
INITIAL_FOOD_MASS = 0
FINAL_FOOD_MASS = 0

#------------------------------------------------------------------ OUTPUTS ------------------------------------------------------------------
STEAM_ACCUMULATION = 0
STEAM_SENSOR_HUMIDITY = 0
STEAM_TEMP = 0
WATER_LOSS = 0



