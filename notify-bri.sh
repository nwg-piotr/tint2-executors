#!/usr/bin/env bash

# Helper to kill notification if any, and display brightness level as a new one

# Dependencies: `xbacklight` or `light-git`, `libnotify`, `xfce4-notifyd` or another notification server

# Prefer the `light` package, use `xbacklight` if `light` not found
if [[ $(which light) == *"/light"* ]]
then
    b=$(light -G)
else
    b=$(xbacklight -get)
fi

# Round the float result
b=$(echo $b | awk '{ printf "%0.0f\n", $1 }')

kill $(ps -e | grep notify | awk '{ print $1 }')
notify-send "$b"% --urgency=low --expire-time=100