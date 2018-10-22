#!/usr/bin/env bash

# This script display an appropriate brightness icon according to the brightness level

# Author: Piotr Miller
# e-mail: nwg.piotr@gmail.com
# Website: http://nwg.pl
# Project: https://github.com/nwg-piotr/tint2-executors
# License: GPL3

# Dependencies: `xbacklight` or `light-git'

# Prefer the `light` package, use `xbacklight` if `light` not found
if [[ $(which light) == *"/light"* ]]
then
    b=$(light -G)
else
    b=$(xbacklight -get)
fi

# Lets round the float result
bri=$(echo "($b+0.5)/1" | bc)

if [ "$bri" -gt "90" ]; then
    echo ~/tint2-executors/images/bri-full.svg
elif [ "$bri" -gt "60" ]; then
    echo ~/tint2-executors/images/bri-high.svg
elif [ "$bri" -gt "40" ]; then
    echo ~/tint2-executors/images/bri-medium.svg
else
    echo ~/tint2-executors/images/bri-low.svg
fi
