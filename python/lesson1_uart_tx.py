import serial

serial_port = serial.Serial('/dev/ttyS0', baudrate=9600, timeout=0.1)

# Loop
while True:
    message_to_send = input("Enter message to send (q for quit): ")

    if message_to_send == 'q':
        print("Recieved q, exiting loop")
        break

    # Write the message to the serial port with a newline appended
    serial_port.write((message_to_send + "\r\n").encode())

    print("Sent message: %s" % message_to_send)
