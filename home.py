import lighting
import powerOutlets
from datetime import datetime

class Home:
    mode = 'Off'
    powerOutlets = powerOutlets.PowerOutlets()
    lighting = lighting.Lighting()

    def __init__(self):
        self.mode = 'init'

    def tick(self, isHome):
        oldMode = self.mode
        self.computeMode(isHome)

        if(oldMode != self.mode):
            self.setMode(self.mode)


    def computeMode(self, isHome):
        now = datetime.now()

        # alarms take priority, doesn't matter if we isHome
        if((now.hour == 7 and now.minute > 40) or (now.hour == 8 and now.minute < 20)):
            self.mode = 'Morning'
            return

        # always set the system mode if we're home
        if(isHome):
            if(now.hour < 5):
                self.mode = 'Night'
            elif(now.hour < 10):
                self.mode = 'Morning'
            elif (now.hour < 20):
                self.mode = 'Light'
            elif (now.hour < 23):
                self.mode = 'Evening'
            else:
                self.mode = 'Night'
        else:
            self.mode = 'Off'

    def setMode(self, mode):
        # set the lighting last because it takes a while to skip unfound btle devs (candles)
        self.powerOutlets.setMode(mode)
        self.lighting.setMode(mode)
