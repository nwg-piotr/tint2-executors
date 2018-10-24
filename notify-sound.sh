#!/usr/bin/env bash

# Helper to kill notification if any and display argument as a new one
# Dependencies: `libnotify`, `xfce4-notifyd` or another notification server

lvl=$(amixer sget Master | grep 'Right:' | awk -F'[][]' '{ print $2 }')

kill $(ps -e | grep notify | awk '{ print $1 }')
notify-send "$lvl" --expire-time=750