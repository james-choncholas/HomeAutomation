import pexpect
from subprocess import Popen, call
import time

class MagicLightBlue:
    my_mac = ''
    secret_bt_handle = '0x002e'
    secret_start_byte = '56'
    secret_color_byte = 'F0'
    secret_white_byte = '0F'
    secret_end_byte = 'AA'

    def __init__(self, mac_str, device_no):
        self.my_mac = mac_str
        #internet says this helps keep stable connection but i didnt need it...
        #call(['sudo', 'hcitool', '-i', device_no, 'lecc', mac_str])

    def turnOff(self):
        self.controlWhite('00')

    def turnOn(self):
        self.controlWhite('FF')

    def controlColor(self, red, green, blue):
        a_str = self.secret_start_byte + red + green + blue + '00' + self.secret_color_byte + self.secret_end_byte
        try:
            call(['sudo', 'gatttool', '-b', self.my_mac, '--char-write', '-a', self.secret_bt_handle, '-n', a_str])
        except:
            pass


    def controlWhite(self, whiteness):
        a_str = self.secret_start_byte + '000000' + whiteness + self.secret_white_byte + self.secret_end_byte
        try:
            call(['sudo', 'gatttool', '-b', self.my_mac, '--char-write', '-a', self.secret_bt_handle, '-n', a_str])
        except:
            pass

    # mode is between 25 and 38, 25 being fade across color spectrum... (see app for details)
    # fifthsOfSecond is the time between each transition
    def fade(self, mode, fifthsOfSecond):
        a_str = 'bb' + mode + fifthsOfSecond + '44'
        try:
            call(['sudo', 'gatttool', '-b', self.my_mac, '--char-write', '-a', self.secret_bt_handle, '-n', a_str])
        except:
            pass
