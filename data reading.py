import smbus
import time
slaveAddress = 0x2f 
i2c = smbus.SMBus(1)
while True:
    byteBlock = i2c.read_i2c_block_data(slaveAddress, 0,28)
    data = ""
    for byteValue in byteBlock:
        data = data + chr(byteValue)
        #a = +1
    print( data)
   # time.sleep(1)

