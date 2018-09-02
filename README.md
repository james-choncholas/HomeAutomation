# Home Automation
Here is some simple code that turns lights on and off in my house.
A raspberry pi 3 scans the 2.4GHz range and whenever it sees my phone's bluetooth
MAC address it turns on MagicLight brand smart bulbs and sets them to different 
colors based on the time of day. It also turns outlets in my house on and off, (thanks 
https://github.com/timleland/rfoutlet.git!) 

# Setup 
Bluetooth Setup:
```
sudo apt-get install bluetooth pi-bluetooth bluez python-bluez
```

RF outlet setup:   
install wiring pi:
```
git clone git://git.drogon.net/wiringPi
    -- or $ cd wiringPi/
./build
```

install driver:
```
sudo git clone https://github.com/timleland/rfoutlet.git /var/www/rfoutlet
    -- or $ sudo cp -r rfoutlet/ /var/www/rfoutlet/
sudo chown root.root /var/www/rfoutlet/codesend
sudo chmod 4755 /var/www/rfoutlet/codesend
```

use RFSniffer to find new outlet codes:
```
sudo /var/www/rfoutlet/RFSniffer
./codesend <code found> -I 198 -p 0
```

Disable onboard wifi (on RPI3) because it conflicts with bluetooth   
add dtoverlay=pi3-disable-wifi   
to the file /boot/config.txt   

Add the following line to /etc/rc.local
(sleep 10 && python /home/pi/HomeAutomation/automation.py) &
