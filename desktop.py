#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""

This script uses `wmctrl` to switch desktops, or just prints path to the icon corresponding to currently active desktop,
followed by the desktop number as text.

Author: Piotr Miller
e-mail: nwg.piotr@gmail.com
Website: http://nwg.pl
Project: https://github.com/nwg-piotr/tint2-executors
License: GPL3

Command: python ~/tint2-executors/desktop.py [-n] | [-p] | [number]

[-n] - switch to next desktop
[-p] - switch to previous desktop
[number] - switch to desktop of number given

"""

import sys
import subprocess
from pathlib import Path


def main():
    output = subprocess.check_output("wmctrl -d", shell=True)
    desktops = output.splitlines()

    current = current_desktop(desktops)
    last = len(desktops) - 1

    if len(sys.argv) > 1:
        if sys.argv[1].upper() == "N" or "-N":
            next_desktop(current, last)
        elif sys.argv[1].upper() == "P" or "-P":
            previous_desktop(current, last)
        else:
            try:
                d = int(sys.argv[1])
                select_desktop(d - 1, last)
            except ValueError:
                print("Argument not allowed. Should be: `desktop.py [-n] | [-p] | [number]`")
    else:
        print(str(Path.home()) + "/tint2-executors/images/desktop.svg")
        print(str(current_desktop(desktops) + 1))


def current_desktop(desktops):
    for d in range(len(desktops)):
        if str(desktops[d]).find("*") > -1:
            return d


def next_desktop(current, last):
    n = current + 1 if current + 1 <= last else 0
    subprocess.call(["wmctrl", "-s", str(n)])


def previous_desktop(current, last):
    n = current - 1 if current - 1 >= 0 else last
    subprocess.call(["wmctrl", "-s", str(n)])


def select_desktop(which, last):
    if 0 <= which <= last:
        subprocess.call(["wmctrl", "-s", str(which)])
    else:
        print("You only have desktops 1-" + str(last + 1))


if __name__ == "__main__":
    main()
