import lightingsystem
from subprocess import Popen, call
import time
import sys
import bluetooth

call(['sudo', 'hciconfig', 'hci0', 'down'])
call(['sudo', 'hciconfig', 'hci0', 'up'])

lighting = lightingsystem.LightingSystem()


while True:
    result = bluetooth.lookup_name("8C:1A:BF:92:EC:85", timeout=2)

    if (result != None):
        print "found!"

        if (not lighting.on):
            lighting.systemOn()
    else:
        print "gone"
        if (lighting.on):
            lighting.systemOff()

    time.sleep(5)
