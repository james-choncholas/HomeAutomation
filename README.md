# Home Automation
Here is some simple code that turns lights on and off in my house
whenever my phone's bluetooth is turned on. Runs on a raspberry pi 3.
It also turns outlets in my house on and off, (thanks 
https://github.com/timleland/rfoutlet.git!) 

# Setup 
Bluetooth Setup:
sudo apt-get install pi-bluetooth
sudo apt-get install bluetooth
sudo apt-get install bluez
sudo apt-get install python-bluez

RF outlet setup:
install wiring pi:
git clone git://git.drogon.net/wiringPi
    -- or $ cd wiringPi/
cd wiringPi
./build

install driver:
sudo git clone https://github.com/timleland/rfoutlet.git /var/www/rfoutlet
    -- or $ sudo cp -r rfoutlet/ /var/www/
sudo chown root.root /var/www/rfoutlet/codesend
sudo chmod 4755 /var/www/rfoutlet/codesend

use RFSniffer to find new outlet codes:
sudo /var/www/rfoutlet/RFSniffer

and run:
./codesend <code found> -I 198 -p 0

Disable onboard wifi (on RPI3) because it conflicts with bluetooth
add dtoverlay=pi3-disable-wifi
to the file /boot/config.txt
