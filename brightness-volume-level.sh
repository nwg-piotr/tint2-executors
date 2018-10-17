#!/usr/bin/env bash

# Author: Piotr Miller
# e-mail: nwg.piotr@gmail.com
# Website: http://nwg.pl
# Project: https://github.com/nwg-piotr/tint2-executors
# License: GPL3

# Dependencies: `alsa-utils`, `xorg-xbacklight` | `light-git`

# Use the line below with `xorg-xbacklight`
bri=B:$(xbacklight -get | cut -d'.' -f1)%

# or replace with the line below for `light-git` (https://github.com/haikarainen/light, should work on Radeon graphics)
# bri=B:$(light -G | cut -d'.' -f1)%

vol=V:$(amixer sget Master | grep 'Right:' | awk -F'[][]' '{ print $2 }')

out=$bri"\n"$vol
echo -e $out
