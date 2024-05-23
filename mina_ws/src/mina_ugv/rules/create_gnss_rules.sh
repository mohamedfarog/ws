echo "start copy 99-ublox-gnss.rules to /etc/udev/rules.d/"
sudo cp 99-ublox-gnss.rules /etc/udev/rules.d

service udev reload
sleep 2
service udev restart
echo "Finish!!!"
