import magiclightblue
import etekCityOutlet
from datetime import datetime

class Home:

    mode = 'Off'
    sideL = magiclightblue.MagicLightBlue("04:a3:16:a7:3b:4e", 'hci0')
    sideR = magiclightblue.MagicLightBlue("04:a3:16:a7:39:61", 'hci0')
    candleS = magiclightblue.MagicLightBlue("88:c2:55:a3:07:89", 'hci0')
    candleM = magiclightblue.MagicLightBlue("88:c2:55:a3:41:0f", 'hci0')
    candleL = magiclightblue.MagicLightBlue("88:c2:55:a3:70:6a", 'hci0')
    outlet1 = etekCityOutlet.EtekCityOutlet('4543795', '4543804')
    outlet2 = etekCityOutlet.EtekCityOutlet('4543939', '4543948')
    outlet3 = etekCityOutlet.EtekCityOutlet('4544259', '4544268')
    outlet4 = etekCityOutlet.EtekCityOutlet('4545795', '4545804')
    outlet5 = etekCityOutlet.EtekCityOutlet('4551939', '4551948')

    def __init__(self):
        self.mode = 'Off'

    def tick(self):
        oldMode = self.mode
        self.computeMode()

        if(oldMode != self.mode):
            self.setMode(self.mode)


    def computeMode(self):
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

    def setMode(self, mode):
        if(mode == 'Morning'):
            self.sideL.controlColor('00', 'FF', '77')
            self.sideR.controlColor('00', 'FF', '77')
            self.candleS.controlColor('00', 'FF', '44')
            self.candleM.controlColor('00', 'FF', '55')
            self.candleL.controlColor('00', 'FF', '66')
            self.outlet1.turnOn()
            self.outlet2.turnOn()
            self.outlet3.turnOn()
            self.outlet4.turnOn()
            self.outlet5.turnOn()
        elif(mode == 'Light'):
            self.sideL.controlWhite('99')
            self.sideR.controlWhite('99')
            self.candleS.controlColor('FF', 'FF', 'FF')
            self.candleM.controlColor('FF', 'FF', 'FF')
            self.candleL.controlColor('FF', 'FF', 'FF')
            self.outlet1.turnOn()
            self.outlet2.turnOn()
            self.outlet3.turnOn()
            self.outlet4.turnOn()
            self.outlet5.turnOn()
        elif(mode == 'Evening'):
            self.sideL.controlColor('FF', '50', '20')
            self.sideR.controlColor('FF', '50', '20')
            self.candleS.fade('25', '50')
            self.candleM.fade('25', '50')
            self.candleL.fade('25', '50')
            self.outlet1.turnOn()
            self.outlet2.turnOn()
            self.outlet3.turnOn()
            self.outlet4.turnOn()
            self.outlet5.turnOn()
        elif(mode == 'Night'):
            self.sideL.controlColor('44', '00', '00')
            self.sideR.controlColor('44', '00', '00')
            self.candleS.fade('2B', '20')
            self.candleM.fade('2B', '20')
            self.candleL.fade('2B', '20')
            self.outlet1.turnOff()
            self.outlet2.turnOff()
            self.outlet3.turnOff()
            self.outlet4.turnOff()
            self.outlet5.turnOff()

    def systemOff(self):
        print "turning system off"
        self.mode = 'Off'
        self.sideL.controlWhite('00')
        self.sideR.controlWhite('00')
        self.candleS.controlColor('00','00','00')
        self.candleM.controlColor('00','00','00')
        self.candleL.controlColor('00','00','00')
        self.outlet1.turnOff()
        self.outlet2.turnOff()
        self.outlet3.turnOff()
        self.outlet4.turnOff()
        self.outlet5.turnOff()
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
