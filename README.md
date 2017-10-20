# HHDash

## Step 0:
* Make sure file is in directory /home/pi/HHDash

## Step 1:
* Run setup.py install

## Step 2:

Add to crontab:

* */1 * * * *  cd /home/pi/Desktop/HHDash/Scripts/ && /usr/bin/python /home/pi/Desktop/HHDash/Scripts/update.py
* @reboot cd /home/pi/Desktop/HHDash/Scripts/ && /usr/bin/python /home/pi/Desktop/HHDash/Scripts/dashboard.py

## Step 3:

Make sure screen doesn’t timeout:

* Turn off display
    * Sudo nano /etc/kbd/config
        * Change 0 and 0
        * https://www.raspberrypi.org/forums/viewtopic.php?t=18200

* Create file  /etc/X11/xorg.conf with this content:
        Section "ServerFlags"
        Option "blank time" "0"
        Option "standby time" "0"
        Option "suspend time" "0"
        Option "off time" "0"
        EndSection

Congratulations, you have successfully configured your very own HackHarvard Dashboard!
