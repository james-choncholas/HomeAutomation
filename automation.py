import home

import sys
from subprocess import call
import time
import bluetooth

call(['sudo', 'hciconfig', 'hci0', 'down'])
call(['sudo', 'hciconfig', 'hci0', 'up'])

home = home.Home()


while True:
    result = bluetooth.lookup_name("8C:1A:BF:92:EC:85", timeout=10)

    home.tick(result != None)

    if(result != None):
        time.sleep(5)
