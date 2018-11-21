#!/bin/sh

# Author: Piotr Miller
# e-mail: nwg.piotr@gmail.com
# Website: http://nwg.pl
# Project: https://github.com/nwg-piotr/tint2-executors
# License: GPL3

# Credits: dsboger/gnome-shell-extension-bumblebee-status
# https://github.com/dsboger/gnome-shell-extension-bumblebee-status
# no-bumblebee icon by @edskeye

if [[ -f "/proc/acpi/bbswitch" ]]; then

    bb_status=$(cat /proc/acpi/bbswitch | awk -F ' ' '{print $2}')
    if [[ "$bb_status" = "ON" ]]; then

        t=$(nvidia-smi -q -d TEMPERATURE | grep "GPU Current Temp" | awk -F ' ' '{ print $5 }')

        echo /usr/share/t2ec/nvidia.svg;
        echo ${t}"℃"

    elif [[ "$bb_status" = "OFF" ]]; then
        echo /usr/share/t2ec/nvidia-off.svg
    fi
else
    echo /usr/share/t2ec/no-bumblebee.svg
fi