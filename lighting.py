import magiclightblue
from mode import Mode

class Lighting:

    sideL = magiclightblue.MagicLightBlue("04:a3:16:a7:3b:4e", 'hci0')
    sideR = magiclightblue.MagicLightBlue("04:a3:16:a7:39:61", 'hci0')
    candleS = magiclightblue.MagicLightBlue("88:c2:55:a3:07:89", 'hci0')
    candleM = magiclightblue.MagicLightBlue("88:c2:55:a3:41:0f", 'hci0')
    candleL = magiclightblue.MagicLightBlue("88:c2:55:a3:70:6a", 'hci0')

    purpleColors = ['e6e6fa', '8a2be2', '9400d3', '9932cc', 'ba55d3', 'da70d6', 'ee82ee', 'ff00ff', 'ee82ee', 'da70d6', 'ba55d3', '9932cc', '9400d3', '8a2be2']
    sunsetColors = ['998040', 'ffa500', 'ff8c00', 'ff7f50', 'ff6347', 'cd5c5c', 'dc143c', '8b0000', 'dc143c', 'cd5c5c', 'ff6347', 'ff7f50', 'ff8c00', 'ffa500']

    def __init__(self):
        return

    def setMode(self, mode):
        if(mode == Mode.Morning):
            self.sideL.fade(self.purpleColors, '1a')
            self.sideR.fade(self.purpleColors, '1a')
            self.candleS.controlColor('00', 'FF', '44')
            #self.candleM.controlColor('00', 'FF', '55')
            #self.candleL.controlColor('00', 'FF', '66')
        elif(mode == Mode.Light):
            self.sideL.controlWhite('99')
            self.sideR.controlWhite('99')
            self.candleS.controlColor('FF', 'FF', 'FF')
            #self.candleM.controlColor('FF', 'FF', 'FF')
            #self.candleL.controlColor('FF', 'FF', 'FF')
        elif(mode == Mode.PreEvening):
            self.sideL.controlColor('FF', '50', '20')
            self.sideR.controlColor('FF', '50', '20')
            self.candleS.mode('25', '50')
            #self.candleM.mode('25', '50')
            #self.candleL.mode('25', '50')
        elif(mode == Mode.Evening):
            self.sideL.fade(self.sunsetColors, '1a')
            self.sideR.fade(self.sunsetColors, '1a')
            self.candleS.mode('25', '50')
            #self.candleM.mode('25', '50')
            #self.candleL.mode('25', '50')
        elif(mode == Mode.Night):
            self.sideL.controlColor('44', '00', '00')
            self.sideR.controlColor('44', '00', '00')
            self.candleS.mode('2B', '20')
            #self.candleM.mode('2B', '20')
            #self.candleL.mode('2B', '20')
        elif(mode == Mode.Alarm):
            self.sideL.mode('26', '01')
            self.sideR.mode('26', '01')
            self.candleS.mode('2B', '01')
            #self.candleM.mode('2B', '01')
            #self.candleL.mode('2B', '01')
        else:
            self.sideL.controlWhite('00')
            self.sideR.controlWhite('00')
            self.candleS.controlColor('00','00','00')
            #self.candleM.controlColor('00','00','00')
            #self.candleL.controlColor('00','00','00')

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
    def systemMode(self, mode, fifthsOfSecond):
        self.sideL.mode(mode, fifthsOfSecond)
        self.sideR.mode(mode, fifthsOfSecond)
        self.candleS.mode(mode, fifthsOfSecond)
        self.candleM.mode(mode, fifthsOfSecond)
        self.candleL.mode(mode, fifthsOfSecond)
