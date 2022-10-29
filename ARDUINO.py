import serial, time

arduino = serial.Serial("COM4", 19200)
time.sleep(2)
arduino.write(b'D')
arduino.close()

