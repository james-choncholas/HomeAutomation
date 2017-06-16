import pexpect
import magiclightblue

class LightingSystem:

    on = False
    sideL = magiclightblue.MagicLightBlue("04:a3:16:a7:3b:4e", 'hci0')
    sideR = magiclightblue.MagicLightBlue("04:a3:16:a7:39:61", 'hci0')
    candleS = magiclightblue.MagicLightBlue("88:c2:55:a3:07:89", 'hci0')
    candleM = magiclightblue.MagicLightBlue("88:c2:55:a3:41:0f", 'hci0')
    candleL = magiclightblue.MagicLightBlue("88:c2:55:a3:70:6a", 'hci0')

    def __init__(self):
        self.on = False

    def systemOn(self):
        print "turning system on"
        self.on = True
        self.sideL.controlWhite('99')
        self.sideR.controlWhite('99')
        self.candleS.controlColor('ff','ff','ff')
        self.candleM.controlColor('ff','ff','ff')
        self.candleL.controlColor('ff','ff','ff')
        print "system on"

    def systemOff(self):
        print "turning system off"
        self.on = False
        self.sideL.controlWhite('00')
        self.sideR.controlWhite('00')
        self.candleS.controlColor('00','00','00')
        self.candleM.controlColor('00','00','00')
        self.candleL.controlColor('00','00','00')
        print "system off"

    # rgb is hex string between '00' and 'FF'
    def systemColor(self, red, green, blue):
        self.on = True
        self.sideL.controlColor(red, green, blue)
        self.sideR.controlColor(red, green, blue)
        self.candleS.controlColor(red, green, blue)
        self.candleM.controlColor(red, green, blue)
        self.candleL.controlColor(red, green, blue)

    # whiteness is decimal string between '00' and '99'
    def systemWhite(self, whiteness):
        self.on = True
        self.sideL.controlWhite(whiteness)
        self.sideR.controlWhite(whiteness)

    # mode is between 25 and 38, 25 being fade across color spectrum... (see app for details)
    # fifthsOfSecond is the time between each transition
    def systemFade(self, mode, fifthsOfSecond):
        self.on = True
        self.sideL.fade(mode, fifthsOfSecond)
        self.sideR.fade(mode, fifthsOfSecond)
        self.candleS.fade(mode, fifthsOfSecond)
        self.candleM.fade(mode, fifthsOfSecond)
        self.candleL.fade(mode, fifthsOfSecond)
