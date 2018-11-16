#!/bin/sh

# Author: Piotr Miller
# e-mail: nwg.piotr@gmail.com
# Website: http://nwg.pl
# Project: https://github.com/nwg-piotr/tint2-executors
# License: GPL3

# Credits: RaphaelRochet/arch-update
# https://github.com/RaphaelRochet/arch-update
# Icon by @edskeye

upd=$(/bin/sh -c "/usr/bin/checkupdates && /usr/bin/trizen -Qqu -a")

if [[ ! -z "$upd" ]]
then
    echo ~/tint2-executors/images/arch-icon-notify.svg
    echo "($upd)" | wc -l
    notify-send "Pending updates:" "<i>$upd</i>" --icon="archlinux" --expire-time=5000
else
    echo ~/tint2-executors/images/arch-icon.svg
fi
