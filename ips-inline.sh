#!/bin/sh

# This script displays external and internal IP address in a single row
# Depends on `bind-tools` (Arch) or `dnsutils` (Debian)

# Author: Piotr Miller
# e-mail: nwg.piotr@gmail.com
# Website: http://nwg.pl
# Project: https://github.com/nwg-piotr/tint2-executors
# License: GPL3

w=$(dig +short myip.opendns.com @resolver1.opendns.com)
l=$(ip addr | grep 'state UP' -A2 | tail -n1 | awk '{print $2}' | cut -f1  -d'/')

echo -e WAN: ${w}" "LAN: ${l}
