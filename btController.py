import lightingsystem

import sys
from subprocess import call
import time
import bluetooth

call(['sudo', 'hciconfig', 'hci0', 'down'])
call(['sudo', 'hciconfig', 'hci0', 'up'])

lighting = lightingsystem.LightingSystem()


while True:
    result = bluetooth.lookup_name("8C:1A:BF:92:EC:85", timeout=10)

    if (result != None):
        lighting.tick()
        time.sleep(5)

    else:
        if (lighting.mode != 'Off'):
            lighting.systemOff()
