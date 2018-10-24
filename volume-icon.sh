#!/usr/bin/env bash

# This script display an appropriate volume icon according to the volume level

# Author: Piotr Miller
# e-mail: nwg.piotr@gmail.com
# Website: http://nwg.pl
# Project: https://github.com/nwg-piotr/tint2-executors
# License: GPL3

# Dependencies: `alsa-utils`, `libnotify`, `xfce4-notifyd` or another notification server

snd=$(amixer sget Master | grep 'Right:' | awk -F'[][]' '{ print $4 }')

if [ "$snd" = "on" ]; then

    vol=$(amixer sget Master | grep 'Right:' | awk -F'[][]' '{ print $2 }')
    v=${vol::-1}

    # Lets round the float result
    v=$(echo "($v+0.5)/1" | bc)

    if [ "$v" -ge "90" ]; then
        echo ~/tint2-executors/images/vol-full.svg
    elif [ "$v" -ge "40" ]; then
        echo ~/tint2-executors/images/vol-medium.svg
    elif [ "$v" -ge "10" ]; then
        echo ~/tint2-executors/images/vol-low.svg
    else
        echo ~/tint2-executors/images/vol-lowest.svg
    fi
else
    echo ~/tint2-executors/images/vol-muted.svg
fi