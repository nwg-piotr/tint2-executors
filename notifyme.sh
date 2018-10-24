#!/usr/bin/env bash

# Helper to kill notification if any and display argument as a new one
# Dependencies: `libnotify`, `xfce4-notifyd` or another notification server

kill $(ps -e | grep notify | awk '{ print $1 }')
notify-send "$1" --expire-time=750