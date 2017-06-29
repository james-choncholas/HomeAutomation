import etekCityOutlet

class PowerOutlets:
    outlet1 = etekCityOutlet.EtekCityOutlet('4543795', '4543804')
    outlet2 = etekCityOutlet.EtekCityOutlet('4543939', '4543948')
    outlet3 = etekCityOutlet.EtekCityOutlet('4544259', '4544268')
    outlet4 = etekCityOutlet.EtekCityOutlet('4545795', '4545804')
    outlet5 = etekCityOutlet.EtekCityOutlet('4551939', '4551948')

    def __init__(self):
        return

    def setMode(self, mode):
        if(mode == 'Morning'):
            self.outlet1.turnOn()
            self.outlet2.turnOn()
            self.outlet3.turnOn()
            self.outlet4.turnOn()
            self.outlet5.turnOn()
        elif(mode == 'Light'):
            self.outlet1.turnOn()
            self.outlet2.turnOn()
            self.outlet3.turnOn()
            self.outlet4.turnOn()
            self.outlet5.turnOn()
        elif(mode == 'Evening'):
            self.outlet1.turnOn()
            self.outlet2.turnOn()
            self.outlet3.turnOn()
            self.outlet4.turnOn()
            self.outlet5.turnOn()
        elif(mode == 'Night'):
            self.outlet1.turnOff()
            self.outlet2.turnOff()
            self.outlet3.turnOff()
            self.outlet4.turnOff()
            self.outlet5.turnOff()
        else:
            self.outlet1.turnOff()
            self.outlet2.turnOff()
            self.outlet3.turnOff()
            self.outlet4.turnOff()
            self.outlet5.turnOff()
