#!/bin/bash

echo "remap the device serial port(ttyUSBX) to rplidar2"
echo "rplidar2 usb connection as /dev/rplidar2, check it using the command : ls -l /dev | grep ttyUSB"
echo "start copy rplidar2.rules to /etc/udev/rules.d/"

sudo cp rplidar2.rules  /etc/udev/rules.d
echo -e "\nRestarting udev\n"
sudo service udev reload
sudo service udev restart
sudo udevadm control --reload && sudo udevadm trigger
echo "finish"
