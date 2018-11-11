#!/bin/sh

# Author: Piotr Miller
# e-mail: nwg.piotr@gmail.com
# Website: http://nwg.pl
# Project: https://github.com/nwg-piotr/tint2-executors
# License: GPL3

# Prefer the `light` package, use `xbacklight` if `light` not found
if [[ $(which light) == *"/light"* ]]
then
    b=$(light -G)
else
    b=$(xbacklight -get)
fi

# Lets round the float result
bri=B:$(echo "($b+0.5)/1" | bc)%

vol=V:$(amixer sget Master | grep 'Right:' | awk -F'[][]' '{ print $2 }')

echo -e ${bri}"\n"${vol}