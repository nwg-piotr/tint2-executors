#!/bin/sh

# This script displays battery icon according to the charge level and charging state

# Author: Piotr Miller
# e-mail: nwg.piotr@gmail.com
# Website: http://nwg.pl
# Project: https://github.com/nwg-piotr/tint2-executors
# License: GPL3

# Dependencies: `acpi`

bat=$(acpi -b)
state=$(echo $bat | awk '{print $3}')

if [ "$state" = "Not" ]; then
    level=$(echo $bat | awk '{print $5}')
    level=${level::-1}

else
    level=$(echo $bat | awk '{print $4}')
    if [[ "$state" == *"Unknown"* ]]; then
        level=${level::-1}
    else
        level=${level::-2}
    fi
fi

if [[ "$bat" == *"until"* ]]; then

    if [ "$level" -ge "95" ]; then
        echo ~/tint2-executors/images/bat-full-charging.svg
    elif [ "$level" -ge "75" ]; then
        echo ~/tint2-executors/images/bat-threefourth-charging.svg
    elif [ "$level" -ge "40" ]; then
        echo ~/tint2-executors/images/bat-half-charging.svg
    elif [ "$level" -ge "15" ]; then
        echo ~/tint2-executors/images/bat-quarter-charging.svg
    else
        echo ~/tint2-executors/images/bat-empty-charging.svg
    fi
else
    if [ "$level" -ge "95" ]; then
        echo ~/tint2-executors/images/bat-full.svg
    elif [ "$level" -ge "75" ]; then
        echo ~/tint2-executors/images/bat-threefourth.svg
    elif [ "$level" -ge "40" ]; then
        echo ~/tint2-executors/images/bat-half.svg
    elif [ "$level" -ge "15" ]; then
        echo ~/tint2-executors/images/bat-quarter.svg
    else
        echo ~/tint2-executors/images/bat-empty.svg
    fi
fi