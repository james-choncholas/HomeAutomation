import magiclightblue
from subprocess import Popen, call
import time
import sys

if len(sys.argv) != 2:
	print "Usage:\n sudo python test.py hciX"
	sys.exit()

device_no = sys.argv[1]

call(['sudo', 'hciconfig', device_no, 'down'])
call(['sudo', 'hciconfig', device_no, 'up'])

x = magiclightblue.MagicLightBlue("04:A3:16:A7:3B:4E", device_no)

x.turnOn()
time.sleep(1)

x.controlColor('FF','00','00')
time.sleep(1)
x.controlColor('00','FF','00')
time.sleep(1)
x.controlColor('00','00','FF')
time.sleep(1)
x.controlWhite('90')
time.sleep(1)

x.fade('25', '01')
time.sleep(20)

x.turnOff()

