echo "start copy imu_usb.rules to /etc/udev/rules.d/"
sudo cp imu_usb.rules /etc/udev/rules.d

echo "start copy rplidar.rules to /etc/udev/rules.d/"
sudo cp rplidar.rules /etc/udev/rules.d

service udev reload
sleep 2
service udev restart
echo "Finish!!!"
