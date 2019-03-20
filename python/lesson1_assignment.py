# TODO: Modify this program to send alice.txt over the serial port
# See https://www.tutorialspoint.com/python/file_readline.htm for an example of this

import serial

serial_port = serial.Serial('/dev/ttyS0', baudrate=9600, timeout=0.1)

# TODO: Open 'alice.txt' assign it to a variable

# Loop
while True:
    # TODO: read through the file with file.readline() and assign each line to message_to_send

    serial_port.write(message_to_send.encode())

    print("Sent message: %s" % message_to_send)
