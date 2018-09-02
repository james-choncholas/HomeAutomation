import lighting
import powerOutlets
from mode import Mode
from datetime import datetime
import time

class Home:
    mode = Mode.Off
    powerOutlets = powerOutlets.PowerOutlets()
    lighting = lighting.Lighting()

    def __init__(self):
        self.mode = 'init'

    def tick(self, isHome):
        oldMode = self.mode
        self.computeMode(isHome)


        if(oldMode != self.mode):
	    print("Setting mode to " + self.mode)
            self.setMode(self.mode)


    def computeMode(self, isHome):
        now = datetime.now()

        # alarms take priority, doesn't matter if we isHome, weekday index starts at 0 = Monday
        if(now.hour == 7 and now.minute > 25 and now.minute < 30 and now.weekday() < 4):
            self.mode = Mode.Alarm
            return

        # always set the system mode if we're home
        if(isHome):
            if(now.hour < 5):
                self.mode = Mode.Night
            elif(now.hour < 10):
                self.mode = Mode.Morning
            elif (now.hour < 20):
                self.mode = Mode.Light
            elif (now.hour < 22 and now.minute < 30):
                self.mode = Mode.PreEvening
            elif (now.hour < 23):
                self.mode = Mode.Evening
            else:
                self.mode = Mode.Night
        else:
            self.mode = Mode.Off

    def setMode(self, mode):
        self.lighting.setMode(mode)
        self.powerOutlets.setMode(mode)
