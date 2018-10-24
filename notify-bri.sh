#!/usr/bin/env bash

# Helper to kill notification if and display volume level as a new one

# Dependencies: `xbacklight` or `light-git`, `libnotify`, `xfce4-notifyd` or another notification server

# Prefer the `light` package, use `xbacklight` if `light` not found
if [[ $(which light) == *"/light"* ]]
then
    b=$(light -G)
else
    b=$(xbacklight -get)
fi

# Round the float result
bri=$(echo "($b+0.5)/1" | bc)%

kill $(ps -e | grep notify | awk '{ print $1 }')
notify-send "$bri" --expire-time=750