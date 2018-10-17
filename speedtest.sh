#!/bin/bash
spd=$(/bin/sh -c "speedtest-cli --simple")
if [ ! -z "$spd" ]
then
    notify-send "$spd"
    date "+%d-%m-%y %H:%M" >> ~/speedtest.txt
    echo $spd >> ~/speedtest.txt
else
    notify-send "Failed measuring speed"
fi
