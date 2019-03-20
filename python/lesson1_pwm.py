import pigpio
from time import sleep

pi = pigpio.pi()

# Define which GPIO we will use for this experiment
INPUT_GPIO = 17
OUTPUT_GPIO = 27

# Configure INPUT_GPIO to INPUT
pi.set_mode(INPUT_GPIO, pigpio.INPUT)

# Configure OUTPUT_GPIO as an output
pi.set_mode(OUTPUT_GPIO, pigpio.OUTPUT)

# Initial duty cycle is completely off
pi.set_PWM_dutycycle(OUTPUT_GPIO, 0)

try:
    # Loop
    while True:
        # If INPUT_GPIO is HIGH
        if pi.read(INPUT_GPIO):
            # Set GPIO OUTPUT_GPIO to 1/2 duty cycle
            pi.set_PWM_dutycycle(OUTPUT_GPIO, 128)

            print("INPUT_GPIO HIGH -> SET OUTPUT_GPIO DUTY CYCLE 1/2")

        # If INPUT_GPIO is LOW
        else:
            # Set OUTPUT_GPIO to 1/8 duty cycle
            pi.set_PWM_dutycycle(OUTPUT_GPIO, 32)

            print("INPUT_GPIO HIGH -> SET OUTPUT_GPIO DUTY CYCLE 1/8")

        # Loop at 10Hz
        sleep(0.1)

except KeyboardInterrupt:
    print("User pressed CTRL+C, ending loop")
