import pirc522 
import signal
import time

rdr = pirc522.RFID()
util = rdr.util()
util.debug = True
print("Waiting for the card")
rdr.wait_for_tag()
(error, data) = rdr.request()

if not error:
 print("Card detected")
 (error, uid) = rdr.anticoll()
 if not error:
  kart_uid = str(uid[0])+" "+str(uid[1])+" "+str(uid[2])+" "+str(uid[3])+" "+str(uid[4])
 print(kart_uid)