#!/usr/bin/env bash

# This script displays battery icon according to the charge level and charging state

# Author: Piotr Miller
# e-mail: nwg.piotr@gmail.com
# Website: http://nwg.pl
# Project: https://github.com/nwg-piotr/tint2-executors
# License: GPL3

# Dependencies: `acpi`

bat=$(acpi -b)
state=$(echo $bat | awk '{print $3}')
if [ "$state" = "Not" ] || [ "$state" = "Unknown," ]; then
    level=$(echo $bat | awk '{print $5}')
    level=${level::-1}
else
    level=$(echo $bat | awk '{print $4}')
    level=${level::-2}
fi

if [ "$state" = "Charging," ] || [ "$state" = "Unknown," ]; then

    if [ "$level" -ge "90" ]; then
        echo ~/tint2-executors/images/bat-full-charging.svg
    elif [ "$level" -ge "40" ]; then
        echo ~/tint2-executors/images/bat-medium-charging.svg
    elif [ "$level" -ge "20" ]; then
        echo ~/tint2-executors/images/bat-low-charging.svg
    else
        echo ~/tint2-executors/images/bat-empty-charging.svg
    fi
else
    if [ "$level" -ge "90" ]; then
        echo ~/tint2-executors/images/bat-full.svg
    elif [ "$level" -ge "40" ]; then
        echo ~/tint2-executors/images/bat-medium.svg
    elif [ "$level" -ge "20" ]; then
        echo ~/tint2-executors/images/bat-low.svg
    else
        echo ~/tint2-executors/images/bat-empty.svg
    fi
fi