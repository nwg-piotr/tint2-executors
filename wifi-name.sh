#!/bin/sh

# Author: Piotr Miller
# e-mail: nwg.piotr@gmail.com
# Website: http://nwg.pl
# Project: https://github.com/nwg-piotr/tint2-executors
# License: GPL3
# Icon by @edskeye

name="none"

wifi=$(iwgetid | awk -F '"' '{ print $2 }')
if [[ ! -z "$wifi" ]]; then
    name="$wifi"
fi

if [[ $1 == -N* ]]; then
    echo "Wi-Fi: $name"
elif [[ $1 == -M* ]]; then
    echo "$(echo $1 | cut -c3-) $name"
else
    echo ~/tint2-executors/images/network.svg
    echo ${name}
fi

