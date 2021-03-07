import time
import board
import digitalio
import busio
import adafruit_mpr121

led = digitalio.DigitalInOut(board.D1)
led.direction = digitalio.Direction.OUTPUT
i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

while True:
    if mpr121.is_touched(0) ==  True:
        print("This banana turns light on")
        led.value = True
    elif mpr121.is_touched(1) == True:
        print("This banana turns the light off")
        led.value = False
    time.sleep(0.5)