#!/bin/sh

# This script display an appropriate volume icon according to the volume level

# Authors: Piotr Miller, @natemaia
# e-mail: nwg.piotr@gmail.com
# Website: http://nwg.pl
# Project: https://github.com/nwg-piotr/tint2-executors
# License: GPL3

# Dependencies: `alsa-utils`

if [[ $1 == up ]]; then
    exec amixer set Master 5%+ unmute -q
elif [[ $1 == down ]]; then
    exec amixer set Master 5%- -q
elif [[ $1 == toggle ]]; then
    exec amixer set Master toggle -q
fi

if [[ "$(amixer sget Master | awk -F'[][]' '/Right:|Mono:/ && NF > 1 {print $4}')" = "on" ]]; then

    # search for the lines containing 'Right:' or 'Mono:', when more than 1 field exists
    # we strip the trailing '%' and round it up with printf "%0.0f" just in case
    vol=$(amixer sget Master | awk -F'[][]' '/Right:|Mono:/ && NF > 1 {sub(/%/, ""); printf "%0.0f\n", $2}')

    if [[ ${vol} -ge 90 ]]; then
        echo /usr/share/t2ec/vol-full.svg
    elif [[ ${vol} -ge 40 ]]; then
        echo /usr/share/t2ec/vol-medium.svg
    elif [[ ${vol} -ge 10 ]]; then
        echo /usr/share/t2ec/vol-low.svg
    else
        echo /usr/share/t2ec/vol-lowest.svg
    fi
    echo ${vol}%
else
    echo /usr/share/t2ec/vol-muted.svg
fi
