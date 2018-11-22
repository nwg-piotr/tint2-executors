#!/bin/sh

# This script display an appropriate brightness icon according to the brightness level

# Author: Piotr Miller
# e-mail: nwg.piotr@gmail.com
# Website: http://nwg.pl
# Project: https://github.com/nwg-piotr/tint2-executors
# License: GPL3

# Dependencies: `xbacklight` or `light-git'

# Prefer the `light` package, use `xbacklight` if `light` not found
if [[ $(which light) == *"/light"* ]]; then
    b=$(light -G)
else
    b=$(xbacklight -get)
fi

# Lets round the float result
bri=$(echo $b | awk '{ printf"%0.0f\n", $1 }')

if [[ "$bri" -gt "90" ]]; then
    echo /usr/share/t2ec/bri-full.svg
elif [[ "$bri" -gt "50" ]]; then
    echo /usr/share/t2ec/bri-high.svg
elif [[ "$bri" -gt "30" ]]; then
    echo /usr/share/t2ec/bri-medium.svg
else
    echo /usr/share/t2ec/bri-low.svg
fi
echo ${bri}%