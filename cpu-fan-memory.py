#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
This script uses the `python-psutil` module to display the CPU average load, frequency (current/max),
the temperature sensor reading, the fan speed and memory usage (used/total).

Author: Piotr Miller
e-mail: nwg.piotr@gmail.com
Website: http://nwg.pl
Project: https://github.com/nwg-piotr/tint2-executors

The script is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License
as published by the Free Software Foundation, either version 3 of the License, or any later version.
The script is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

Inspired by tknomanzr's cpu.py at https://forums.bunsenlabs.org/viewtopic.php?id=4276

Command: python ~/tint2-executors/cpu-fan-memory.py [-options]

Optional argument: -GPAFS (case insensitive)

- [G]raphical CPU load bar
- [P]ercentage for each core (text)
- [A]verage CPU load (txt)
- [F]ahrenheit instead of ℃
- [S]hort - omit max CPU frequency and total memory value

Note: avoid combining A with P and G - this will slow the script down. See the project Wiki for more details.
"""

import sys
import psutil


def main():
    display_graph = True
    display_average = False
    display_percentage = False
    short = False
    fahrenheit = False

    if len(sys.argv) > 1 and sys.argv[1].startswith("-"):
        options = sys.argv[1][1:].upper()
        short = options.find("S") > -1
        display_average = options.find("A") > -1
        display_percentage = options.find("P") > -1
        display_graph = options.find("G") > -1
        fahrenheit = options.find("F") > -1

    if not display_average and not display_percentage:
        display_graph = True

    # CPU load
    if display_graph or display_percentage:

        result = psutil.cpu_percent(interval=1, percpu=True)

        if display_graph:
            # Load per CPU as semi-graph:
            print(graph_per_cpu(result), end=" ")

        if display_percentage:
            # Load per CPU as percentage:
            print("CPU%: " + per_cpu(result), end = "")

    if display_average:
        # CPU average load:
        print("CPU: " + str(psutil.cpu_percent(interval=1)), end = "% ")

    # CPU frequency
    try:
        freq = psutil.cpu_freq(False)
        if freq is not None:
            print(str(round(freq[0] / 1000, 1)), end="")
            if not short:
                print("/" + str(round(freq[2] / 1000, 1)), end="")
            print("GHz", end=" ")
    except:
        pass

    # Temperature sensor
    try:
        temp = psutil.sensors_temperatures(fahrenheit)      # True for Fahrenheit
        if len(temp) > 0:                                   # Temperature sensor found!
            core_temp = temp["coretemp"]                    # "acpitz" for ACPI Thermal Zone
            print(core_temp[0][1], end="℉" if fahrenheit else "℃")
    except:
        pass

    # Fan speed
    try:
        fans = psutil.sensors_fans()
        if len(fans) > 0:                                   # Fan sensor found!
            fan0 = next(iter(fans.values()))
            print(" " + str(fan0[0][1]), end="/m ")
        else:
            print(" ", end = "")
    except:
        pass

    # Memory: used/total
    memory = psutil.virtual_memory()
    print(str(round((memory[0] - memory[1]) / 1073741824, 1)), end="")
    if not short:
        print("/" + str(round(memory[0] / 1073741824, 1)), end="")
    print("GB ")


def per_cpu(result):
    string = ""
    for val in result:
        proc = str(int(round(val, 1)))
        if len(proc) < 2:
            proc = "0" + proc
        string += proc + " "
    return string


def graph_per_cpu(result):

    # Un-hash the pattern you like below or replace with your own:
    graph = "_▁▂▃▄▅▆▇███"
    # graph = " ⢀⣀⣠⣤⣴⣶⣾⣿⣿⣿"

    string = ""
    for val in result:
        proc = int(round(val / 10, 0))
        string += graph[proc]
    return string


if __name__ == "__main__":
    main()
