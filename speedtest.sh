#!/bin/sh

# Author: Piotr Miller
# e-mail: nwg.piotr@gmail.com
# Website: http://nwg.pl
# Project: https://github.com/nwg-piotr/tint2-executors
# License: GPL3

spd=$(/bin/sh -c "speedtest-cli --simple")
if [ ! -z "$spd" ]
then
    notify-send "$spd"
    date "+%d-%m-%y %H:%M" >> ~/speedtest.txt
    echo $spd >> ~/speedtest.txt
else
    notify-send "Failed measuring speed"
fi
