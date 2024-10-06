import time
import RPi.GPIO as GPIO

# Use BCM or BOARD pin numbering
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin connected to the LED strip data input
LED_PIN = 24

# Set up the LED_PIN as an output
GPIO.setup(LED_PIN, GPIO.OUT)

# Define colors as PWM duty cycles (for simplicity, assume single color control)
red_duty_cycle = 100  # Full brightness
blue_duty_cycle = 50  # Half brightness

# Initialize PWM on the LED_PIN at 800Hz frequency
pwm = GPIO.PWM(LED_PIN, 800)
pwm.start(0)  # Start with LED off

try:
    while True:
        # Turn LEDs red
        pwm.ChangeDutyCycle(red_duty_cycle)
        time.sleep(1)
        
        # Turn LEDs blue
        pwm.ChangeDutyCycle(blue_duty_cycle)
        time.sleep(1)

except KeyboardInterrupt:
    pass

finally:
    pwm.stop()
    GPIO.cleanup()
