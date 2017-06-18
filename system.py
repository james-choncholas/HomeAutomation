import magiclightblue

from datetime import datetime

class LightingSystem:

    mode = 'Off'
    sideL = magiclightblue.MagicLightBlue("04:a3:16:a7:3b:4e", 'hci0')
    sideR = magiclightblue.MagicLightBlue("04:a3:16:a7:39:61", 'hci0')
    candleS = magiclightblue.MagicLightBlue("88:c2:55:a3:07:89", 'hci0')
    candleM = magiclightblue.MagicLightBlue("88:c2:55:a3:41:0f", 'hci0')
    candleL = magiclightblue.MagicLightBlue("88:c2:55:a3:70:6a", 'hci0')

    def __init__(self):
        self.mode = 'Off'

    def tick(self):
        oldMode = self.mode
        self.setMode()

        if(oldMode != self.mode):
            self.setLighting(self.mode)


    def setMode(self):
        if(datetime.now().hour < 5):
            self.mode = 'Night'
        elif(datetime.now().hour < 10):
            self.mode = 'Morning'
        elif (datetime.now().hour < 19):
            self.mode = 'Light'
        elif (datetime.now().hour < 22):
            self.mode = 'Evening'
        else:
            self.mode = 'Night'

    def setLighting(self, mode):
        if(mode == 'Morning'):
            self.sideL.controlColor('00', 'FF', '77')
            self.sideR.controlColor('00', 'FF', '77')
            self.candleS.controlColor('00', 'FF', '44')
            self.candleM.controlColor('00', 'FF', '55')
            self.candleL.controlColor('00', 'FF', '66')
        elif(mode == 'Light'):
            self.sideL.controlWhite('99')
            self.sideR.controlWhite('99')
            self.candleS.controlColor('FF', 'FF', 'FF')
            self.candleM.controlColor('FF', 'FF', 'FF')
            self.candleL.controlColor('FF', 'FF', 'FF')
        elif(mode == 'Evening'):
            self.sideL.controlColor('FF', '50', '20')
            self.sideR.controlColor('FF', '50', '20')
            self.candleS.fade('25', '50')
            self.candleM.fade('25', '50')
            self.candleL.fade('25', '50')
        elif(mode == 'Night'):
            self.sideL.controlColor('99', '00', '00')
            self.sideR.controlColor('99', '00', '00')
            self.candleS.fade('2B', '20')
            self.candleM.fade('2B', '20')
            self.candleL.fade('2B', '20')

    def systemOff(self):
        print "turning system off"
        self.mode = 'Off'
        self.sideL.controlWhite('00')
        self.sideR.controlWhite('00')
        self.candleS.controlColor('00','00','00')
        self.candleM.controlColor('00','00','00')
        self.candleL.controlColor('00','00','00')
        print "system off"

    # rgb is hex string between '00' and 'FF'
    def systemColor(self, red, green, blue):
        self.sideL.controlColor(red, green, blue)
        self.sideR.controlColor(red, green, blue)
        self.candleS.controlColor(red, green, blue)
        self.candleM.controlColor(red, green, blue)
        self.candleL.controlColor(red, green, blue)

    # whiteness is decimal string between '00' and '99'
    def systemWhite(self, whiteness):
        self.sideL.controlWhite(whiteness)
        self.sideR.controlWhite(whiteness)

    # mode is between 25 and 38, 25 being fade across color spectrum... (see app for details)(increments in hex)
    # fifthsOfSecond is the time between each transition
    def systemFade(self, mode, fifthsOfSecond):
        self.sideL.fade(mode, fifthsOfSecond)
        self.sideR.fade(mode, fifthsOfSecond)
        self.candleS.fade(mode, fifthsOfSecond)
        self.candleM.fade(mode, fifthsOfSecond)
        self.candleL.fade(mode, fifthsOfSecond)
