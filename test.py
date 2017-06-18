import magiclightblue
import etekCityOutlet
from subprocess import Popen, call
import time
import sys

o1 = etekCityOutlet.EtekCityOutlet('4543795', '4543804')
o2 = etekCityOutlet.EtekCityOutlet('4543939', '4543948')
o3 = etekCityOutlet.EtekCityOutlet('4544259', '4544268')
o4 = etekCityOutlet.EtekCityOutlet('4545795', '4545804')
o5 = etekCityOutlet.EtekCityOutlet('4551939', '4551948')

o4.turnOn()

time.sleep(2)

o4.turnOff()
