raspberry-pi-gps-tracker
========================

Some scripts turning the Raspberry Pi into a GPS tracker.

My hardware used for this project is:

 * A Raspberry Pi (model B).
 * A Bluetooth dongle.
 * A Holux M-1200 Bluetooth GPS.

This could probably be used with other hardware as well.

gpst.py is a simple script checking GPS device for location and reporting that location to a website once in a while.

Copy settings-example.py to settings.py and tune it to your needs.

If you want to use this on the go, I'd recommend using a 3G-modem and the excellent Sakis3G script to connect to the internet: <http://www.sakis3g.org/>.
