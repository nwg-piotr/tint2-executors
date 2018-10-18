#!/usr/bin/env bash

# Author: Piotr Miller
# e-mail: nwg.piotr@gmail.com
# Website: http://nwg.pl
# Project: https://github.com/nwg-piotr/tint2-executors
# License: GPL3

# Credits: RaphaelRochet/arch-update
# https://github.com/RaphaelRochet/arch-update

upd=$(/bin/sh -c "/usr/bin/checkupdates && /usr/bin/trizen -Qqu -a")

if [ ! -z "$upd" ]
then
    echo ~/.ob-arch-checker/arch-icon-notify.svg
    notify-send "Pending updates:" "<i>$upd</i>" --icon="archlinux" --expire-time=5000
else
    echo ~/.ob-arch-checker/arch-icon.svg
fi
