# This script controls a reapberry pi with python.
# It will turn 10 LED's in a WS2811 strip.
# They will turn on red then blue every 1 second.
# The pins should be connected as follows:
# 5V to 5V
# GND to GND
# DIN to board.D18 (Which is GPIO 18)


import time
import board
import neopixel

# Define the number of pixels in the strip
num_pixels = 10

# Define the pin the strip is connected to
pixel_pin = board.D24

# Define the order of the pixel colors - RGB or GRB
ORDER = neopixel.GRB

# Define the brightness of the pixels
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

# Define the colors
red = (255, 0, 0)
blue = (0, 0, 255)

# Define the delay
delay = 1

# Define the loop
while True:
    for i in range(num_pixels):
        pixels[i] = red
    pixels.show()
    time.sleep(delay)
    for i in range(num_pixels):
        pixels[i] = blue
    pixels.show()
    time.sleep(delay)

# End of script
