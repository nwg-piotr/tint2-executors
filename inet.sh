#!/usr/bin/env bash

# This script displays Internet DL/UL speed, external and internal IP address in a single row
# Dependencies: `speedtest-cli`, `bind-tools` (Arch) or `dnsutils` (Debian)

# Author: Piotr Miller
# e-mail: nwg.piotr@gmail.com
# Website: http://nwg.pl
# Project: https://github.com/nwg-piotr/tint2-executors
# License: GPL3

spd=$(speedtest-cli --simple)
dl=$(echo $spd | awk '{print $5}')
ul=$(echo $spd | awk '{print $8}')

w=$(dig +short myip.opendns.com @resolver1.opendns.com)
l=$(ip addr | grep 'state UP' -A2 | tail -n1 | awk '{print $2}' | cut -f1  -d'/')

echo -e SPD: ${dl}/${ul} Mbit/s WAN: ${w} LAN: ${l}

# Log results to the text file
date "+%d-%m-%y %H:%M" >> ~/speedtest.txt
echo $spd >> ~/speedtest.txt