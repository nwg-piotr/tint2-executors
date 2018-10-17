#!/usr/bin/env bash

# Author: Piotr Miller
# e-mail: nwg.piotr@gmail.com
# Website: http://nwg.pl
# Project: https://github.com/nwg-piotr/tint2-executors
# License: GPL3

# Use the line below with `xorg-xbacklight`
bri=B:$(xbacklight -get | cut -d'.' -f1)%

# or replace with the line below to use the `light` package (should work with Radeon graphics)
# bri=B:$(light -G | cut -d'.' -f1)%

vol=V:$(amixer sget Master | grep 'Right:' | awk -F'[][]' '{ print $2 }')

out=$bri"\n"$vol
echo -e $out
