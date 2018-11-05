#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
ATTENTION: THIS SCRIPT IS UNDER DEVELOPMENT, NOT YET READY TO USE

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

Command: python ~/tint2-executors/cpu-fan-memory.py [-C{components}] [-F]

Optional arguments: -CgpaStfM -F

-C stands for Components:
    g - (g)raphical CPU load bar
    p - (p)ercentage for each core (text)
    a - (a)verage CPU load (text)
    s - current CPU (s)peed
    S - current/max CPU (S)peed
    t - CPU (t)emperature
    f - (f)an speed
    m - (m)emory in use
    M - (M)emory in use/total
-F - use Fahrenheit instead of ℃
-T - test execution time

Note: Combining `g` or `p` with `a` slows the script down twice.

"""

import sys
import psutil
import re
import time


def main():

    fahrenheit = False
    testing = False
    time_start = None
    components = None

    for i in range(1, len(sys.argv)):
        if sys.argv[i] == "-F":
            fahrenheit = True

        if sys.argv[i] == "-T":
            testing = True

        if sys.argv[i].startswith("-C"):
            components = sys.argv[i][2::]

    if components is None:
        components = "gStfM"

    if testing:
        time_start = int(round(time.time() * 1000))

    pcpu, avg, speed, temp = None, None, None, None
    output = ""

    # prepare requested data only once
    if "g" in components or "p" in components:
        pcpu = psutil.cpu_percent(interval=1, percpu=True)

    if "a" in components:
        avg = psutil.cpu_percent(interval=1)

    if "s" in components or "S" in components:
        try:
            speed = psutil.cpu_freq(False)
        except:
            pass

    if "t" in components:
        temp = psutil.sensors_temperatures(fahrenheit)

    for char in components:
        if char == "g":
            output += " " + graph_per_cpu(pcpu) + " "

        if char == "p":
            output += " " + per_cpu(pcpu) + " "

        if char == "a":
            output += " CPU: " + str(avg) + "% "

        if char == "s" and speed is not None:
            output += " " + str(round(speed[0] / 1000, 1)) + "GHz "

        if char == "S" and speed is not None:
            output += " " + str(round(speed[0] / 1000, 1)) + "/" + str(round(speed[2] / 1000, 1)) + "GHz "

        if char == "t" and temp is not None and len(temp) > 0:
            # Change to "acpitz" for ACPI Thermal Zone
            output += " " + str(temp["coretemp"][0][1])
            output += "℉ " if fahrenheit else "℃ "

    # remove double spaces and print
    print(re.sub(' +', ' ', output))

    if testing:
        print("\nIt took " + str(int((round(time.time() * 1000)) - time_start) / 1000) + " s")

    exit(0)

    display_graph = True
    display_average = False
    display_percentage = False
    short = False

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
        string += proc + "% "
    return string


def graph_per_cpu(result):

    graph = "_▁▂▃▄▅▆▇███"

    string = ""
    for val in result:
        proc = int(round(val / 10, 0))
        string += graph[proc]
    return string


if __name__ == "__main__":
    main()
