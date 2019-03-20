import serial

serial_port = serial.Serial('/dev/tty.usbserial-FTZ8B103', baudrate=9600, timeout=0.1)

try:
    # Loop
    while True:
        message_received = serial_port.readline()
        if message_received != b'':
            print("%s" % str(message_received))

except KeyboardInterrupt:
    print("User pressed CTRL+C, ending loop")
