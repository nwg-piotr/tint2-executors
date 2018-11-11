#!/bin/sh

# Helper to kill notification if and display volume level as a new one

# Dependencies: `alsa-utils`, `libnotify`, `xfce4-notifyd` or another notification server

lvl=$(amixer sget Master | grep 'Right:' | awk -F'[][]' '{ print $2 }')

kill $(ps -e | grep notify | awk '{ print $1 }')
notify-send "$lvl" --expire-time=750