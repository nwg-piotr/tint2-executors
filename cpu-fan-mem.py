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

Command: python ~/tint2-executors/cpu-fan-mem.py [-C{components}] [-F] [-T]

Optional arguments: -CgpaStfM -F -T

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
    components = "gStfM"

    for i in range(1, len(sys.argv)):
        if sys.argv[i] == "-F":
            fahrenheit = True

        if sys.argv[i] == "-T":
            testing = True

        if sys.argv[i].startswith("-C"):
            components = sys.argv[i][2::]

    if testing:
        time_start = int(round(time.time() * 1000))

    pcpu, avg, speed, temp, fans, memory = None, None, None, None, None, None
    output = ""

    # prepare ONLY requested data, ONLY once
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

    if "f" in components:
        try:
            fans = psutil.sensors_fans()
        except:
            pass

    if "m" in components or "M" in components:
        memory = psutil.virtual_memory()

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
            # "acpitz" for ACPI Thermal Zone
            output += " " + str(temp["coretemp"][0][1])
            output += "℉ " if fahrenheit else "℃ "

        if char == "f" and fans is not None and len(fans) > 0:
            fan0 = next(iter(fans.values()))
            output += " " + str(fan0[0][1]) + "/m "

        if char == 'm' and memory is not None:
            output += " " + str(round((memory[0] - memory[1]) / 1073741824, 1)) + "GB "

        if char == 'M' and memory is not None:
            output += " " + str(round((memory[0] - memory[1]) / 1073741824, 1)) + "/" + str(
                round(memory[0] / 1073741824, 1)) + "GB "

    if testing:
        output += " [" + str(int((round(time.time() * 1000)) - time_start) / 1000) + "s]"

    # remove double, leading and trailing spaces before printing
    print(re.sub(' +', ' ', output).strip())


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
