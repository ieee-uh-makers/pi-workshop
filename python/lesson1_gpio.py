import pigpio

pi = pigpio.pi()

# Define which GPIO we will use for this experiment
INPUT_GPIO = 17
OUTPUT_GPIO = 27

# Configure INPUT_GPIO as an input
pi.set_mode(INPUT_GPIO, pigpio.INPUT)

# Configure OUTPUT_GPIO as an output
pi.set_mode(OUTPUT_GPIO, pigpio.OUTPUT)

# If INPUT_GPIO is HIGH
if pi.read(INPUT_GPIO):
    # Set OUTPUT_GPIO to on
    pi.write(OUTPUT_GPIO, 1)

    print("INPUT_GPIO HIGH -> SET OUTPUT_GPIO HIGH")

# If INPUT_GPIO is LOW
else:
    # Set OUTPUT_GPIO to off
    pi.write(OUTPUT_GPIO, 0)

    print("INPUT_GPIO HIGH -> SET OUTPUT_GPIO LOW")
