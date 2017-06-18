from subprocess import call
import time

class EtekCityOutlet:
    onCode = ''
    offCode = ''
    pulseLength = '179'
    antenna_gpio = '0'

    def __init__(self, on_code, off_code):
        self.onCode = on_code
        self.offCode = off_code

    def turnOn(self):
        try:
            call(['/var/www/rfoutlet/codesend', self.onCode, '-l', self.pulseLength, '-p', self.antenna_gpio])
        except:
            pass

    def turnOff(self):
        try:
            call(['/var/www/rfoutlet/codesend', self.offCode, '-l', self.pulseLength, '-p', self.antenna_gpio])
        except:
            pass

