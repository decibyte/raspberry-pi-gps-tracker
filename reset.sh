#!/bin/bash

# This is a script I use when there seems to be a problem with the GPS.
# I Don't know if all of it is necessary, but it works (most of the
# time).
#
# I'm using a Bluetooth rfcomm configuration similar to the one found
# at: <http://www.catb.org/gpsd/bt.html>

echo "******************************************************"
echo """
 Procedure:
 * Remove BT dongle form Pi
 * Turn on Pi
 * Turn on GPS
 * Plug in BT dongle
 * Make sure it's working (blue light blinking)
 * Run this script
"""
echo "******************************************************"
sudo service bluetooth restart
sleep 5
sudo rfcomm release /dev/rfcomm0
sleep 1
sudo rfcomm bind rfcomm0
sleep 5
sudo service gpsd restart
sleep 5
echo "******************************************************"
echo " Should be ready now. Try running one of the scripts. "
echo "******************************************************"
