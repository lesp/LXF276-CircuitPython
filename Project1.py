import time
import board
import digitalio

print("hello world")

led = digitalio.DigitalInOut(board.D17)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.1)
    led.value = False
    time.sleep(0.1)
