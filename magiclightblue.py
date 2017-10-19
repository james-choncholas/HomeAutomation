from subprocess import call
import time

class MagicLightBlue:
    my_mac = ''
    bt_handle = '0x002e'
    start_single_color = '56'
    end_single_color = 'AA'
    end_rgb_cmd = 'F0'
    end_white_cmd = '0F'
    start_multi_color = '99'
    end_multi_color = '3aff66'

    def __init__(self, mac_str, device_no):
        self.my_mac = mac_str
        #internet says this helps keep stable connection but i didnt need it...
        #call(['sudo', 'hcitool', '-i', device_no, 'lecc', mac_str])

    def turnOff(self):
        self.controlWhite('00')

    def turnOn(self):
        self.controlWhite('FF')

    def controlColor(self, red, green, blue):
        a_str = self.start_single_color + red + green + blue + '00' + self.end_rgb_cmd + self.end_single_color
        self.send(a_str)


    def controlWhite(self, whiteness):
        a_str = self.start_single_color + '000000' + whiteness + self.end_white_cmd + self.end_single_color
        self.send(a_str)

    # mode is between 25 and 38, 25 being fade across color spectrum... (see app for details)
    # fifthsOfSecond is the time between each transition
    def mode(self, mode, fifthsOfSecond):
        a_str = 'bb' + mode + fifthsOfSecond + '44'
        self.send(a_str)

    # listOfColorStrings is specified as such ['FF0000', '00F0F0', 'F00080']
    # fifthsOfSecond is the time between each transition, do not send 0
    def fade(self, listOfColorStrings, fifthsOfSecond):

        a_str = '' + self.start_multi_color
        numColors = 0

        for rgbString in listOfColorStrings:
           a_str += rgbString
           numColors += 1

        if(numColors > 16):
            print 'Too many colors. max is 16'
            return

        while(numColors < 16):
            a_str += '010203'#yes, the color 010203 is hardcoded to be 'unused'
            numColors += 1

        a_str += fifthsOfSecond + self.end_multi_color
        self.send(a_str)


    def send(self, a_string):
        try:
            call(['sudo', 'gatttool', '-b', self.my_mac, '--char-write-req', '-a', self.bt_handle, '-n', a_string])
        except:
            # try again
            try:
                call(['sudo', 'gatttool', '-b', self.my_mac, '--char-write-req', '-a', self.bt_handle, '-n', a_string])
            except:
                pass
