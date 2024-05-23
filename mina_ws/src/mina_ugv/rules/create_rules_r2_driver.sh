#!/bin/bash

echo "remap the device serial port(ttyUSBX) to r2_driver"
echo "r2_driver usb connection as /dev/r2_driver, check it using the command : ls -l /dev | grep ttyUSB"
echo "start copy r2_driver.rules to /etc/udev/rules.d/"
source /usr/share/colcon_cd/function/colcon_cd.sh
sudo cp r2_driver.rules  /etc/udev/rules.d
echo -e "\nRestarting udev\n"
sudo service udev reload
sudo service udev restart
sudo udevadm control --reload && sudo udevadm trigger
echo "finish"
