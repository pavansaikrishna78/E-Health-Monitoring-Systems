import thingspeak
import time
import math
import time
import serial
import re

channel_id = 1667349 # CHANNEL ID 
write_key  = 'ES2E9O42G3E20CSF' # WRITE KEY 
read_key   = '0XF5R0SAOLSUGEUX' # READ KEY





def measure(channel):
    try:
        
        ser=serial.Serial('/dev/ttyUSB0',9600) # Read data from USB port
        readedText = ser.readline()
        print(readedText)
        ser.close()

        text = readedText.decode('utf-8') #"b'85.00,12.84,80.15\r\n'"
        nums = re.findall(r'\b\d{1,3}(?:,\d{3})*(?:\.\d+)?(?!\d)', text)
        print(nums)
        #x=int(nums[0]+1
        for i in range(0, len(nums)):
            nums[i] = float(nums[i])
            print(nums)
    
        response = channel.update({'field1': nums[0], 'field2': nums[1], 'field3': nums[2]})
        read = channel.get({})
        print("Read:", read)
        
    except:
        print("connection failed")
        
        
if __name__ == "__main__":
    channel = thingspeak.Channel(id=channel_id, api_key=write_key)
    while True:
        measure(channel)
        # Free account has an api limit of 15sec
        time.sleep(15)
