#!/usr/bin/env python

"""
This script uses the python-psutil module to display the CPU average load, frequency (current/max),
the temperature sensor reading, the fan speed and memory usage (used/total).

Author: Piotr Miller
e-mail: nwg.piotr@gmail.com
website: http://nwg.pl

The script is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License
as published by the Free Software Foundation, either version 3 of the License, or any later version.
Obhud is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

Inspired by tknomanzr's cpu.py at https://forums.bunsenlabs.org/viewtopic.php?id=4276

Executor: `python ~/tint2-executors/cpu-fan-memory.py`
Arguments (optional): -a (average CPU load) | -p (textual percentage for each core) | -g (graphical CPU load bar)
Combining -ag will slow the script down - not recommended
Add `-s` argument to omit max CPU frequency and total memory value
"""

import sys
import psutil


def main():
    display_average = False
    display_percentage = False
    short = False

    if len(sys.argv) > 1 and sys.argv[1].startswith("-"):
        options = sys.argv[1][1:].upper()
        print(options)
        short = options.find("S") > -1
        display_average = options.find("A") > -1
        display_percentage = options.find("P") > -1
        display_graph = options.find("G") > -1
    else:
        display_graph = True

    # CPU load

    if display_graph or display_percentage:

        result = psutil.cpu_percent(interval=1, percpu=True)

        if display_graph:
            # Display load per CPU as semi-graph:
            print(graph_per_cpu(result), end=" ")

        if display_percentage:
            # Load per CPU as percentage:
            print("CPU%: " + per_cpu(result), end = "")

    if display_average:
        # CPU average load:
        print("CPU: " + str(psutil.cpu_percent(interval=1)), end = "% ")

    # CPU frequency
    freq = psutil.cpu_freq(False)
    if freq is not None:
        print(str(round(freq[0] / 1000, 1)), end="")
        if not short:
            print("/" + str(round(freq[2] / 1000, 1)), end="")
        print("GHz")

    # Temperature sensor
    temp = psutil.sensors_temperatures(False)       # True for Fahrenheit
    if len(temp) > 0:                               # Temperature sensor found
        core_temp = temp["coretemp"]                # "acpitz" for ACPI Thermal Zone
        print(core_temp[0][1], end = "℃")

    # Fan speed
    fans = psutil.sensors_fans()
    if len(fans) > 0:                               # fan sensor found
        fan0 = next(iter(fans.values()))
        print(" " + str(fan0[0][1]), end="/m ")
    else:
        print(" ", end = "")

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

