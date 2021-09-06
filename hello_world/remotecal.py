import time
import serial
import configuration_modbus as CONF

ser = serial.Serial(port=CONF.PORT, baudrate=CONF.BAUD_RATE, parity=serial.PARITY_NONE,
                    bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE, timeout=CONF.TIMEOUT)
if ser.isOpen():
    ser.close()
ser.open()
ser.isOpen()


def WallOpen():
    ser.write(bytes(b"#OPEN_ZERO$"))

def Readings():
    readings = ser.write(bytes(b"#READING$"))

    readings.split(", ")
    print(readings)



# ser.write(bytes(b"#OPEN_ZERO$"))
# ser.write(bytes(b"#READING$"))
# ser.write(bytes(b"#CLOSE_ZERO$"))
# ser.write(bytes(b"#OPEN_SPAN,CO$"))
# ser.write(bytes(b"#CHKSPAN,CO,500$"))
# ser.write(bytes(b"#CLOSE_SPAN,CO$"))
out = ''
# let's wait one second before reading output (let's give device time to answer)
time.sleep(1)
while ser.inWaiting() > 0:
    out = ser.read(40)

if out != '':
    print(out)

ser.close()
