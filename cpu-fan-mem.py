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

Command: python ~/tint2-executors/cpu-fan-mem.py [-C{components}] [-F] [-T] [-N]

Optional arguments: -CgpaQStfM -F -T -N

-C stands for Components:
    g - (g)raphical CPU load bar
    p - (p)ercentage for each core (text)
    a - (a)verage CPU load (text)
    q - fre(q)ency for each thread
    Q - fre(Q)ency for each thread/max frequency
    s - current CPU (s)peed
    S - current/max CPU (S)peed
    t - CPU (t)emperature
    f - (f)an speed
    m - (m)emory in use
    M - (M)emory in use/total
-F - use Fahrenheit instead of ℃
-N - display field names (except for (g)raphical CPU load bar)
-T - test execution time

Note: Combining `g` or `p` with `a` slows the script down twice.

"""

import sys
import psutil
import re
import time


def main():
    fahrenheit = False
    names = False
    testing = False
    time_start = None
    components = "gStfM"

    for i in range(1, len(sys.argv)):
        if sys.argv[i] == "-F":
            fahrenheit = True

        if sys.argv[i] == "-N":
            names = True

        if sys.argv[i] == "-T":
            testing = True

        if sys.argv[i].startswith("-C"):
            components = sys.argv[i][2::]

    if testing:
        time_start = int(round(time.time() * 1000))

    pcpu, avg, speed, freqs, temp, fans, memory = None, None, None, None, None, None, None
    output = ""

    # Prepare ONLY requested data, ONLY once
    if "g" in components or "p" in components:
        try:
            pcpu = psutil.cpu_percent(interval=1, percpu=True)
        except:
            pass

    if "a" in components:
        try:
            avg = str(psutil.cpu_percent(interval=1))
            if len(avg) < 4:
                avg = "~" + avg
        except:
            pass

    if "s" in components or "S" in components:
        try:
            speed = psutil.cpu_freq(False)
        except:
            pass

    if "q" in components or "Q" in components:
        try:
            freqs = psutil.cpu_freq(True)
        except:
            pass

    if "t" in components:
        try:
            temp = psutil.sensors_temperatures(fahrenheit)
        except:
            pass

    if "f" in components:
        try:
            fans = psutil.sensors_fans()
        except:
            pass

    if "m" in components or "M" in components:
        try:
            memory = psutil.virtual_memory()
        except:
            pass

    # Build output component after component
    for char in components:
        if char == "g" and pcpu is not None:
            #output += " CPU:" if names else " "
            output += " " + graph_per_cpu(pcpu) + " "

        if char == "p" and pcpu is not None:
            output += " CPU:" if names else " "
            output += per_cpu(pcpu) + " "

        if char == "a" and avg is not None:
            output += " avCPU:" if names else " "
            output += avg + "% "

        if char == "q" and freqs is not None:
            output += " CPU:" if names else " "
            output += freq_per_cpu(freqs)[0][:-1] + "GHz "

        if char == "Q" and freqs is not None:
            output += " CPU:" if names else " "
            result = freq_per_cpu(freqs)
            output += result[0][:-1] + "/" + result[1] + "GHz "

        if char == "s" and speed is not None:
            output += " SPD:" if names else " "
            output += str(round(speed[0] / 1000, 1)) + "GHz "

        if char == "S" and speed is not None:
            output += " avSPD:" if names else " "
            output += str(round(speed[0] / 1000, 1)) + "/" + str(round(speed[2] / 1000, 1)) + "GHz "

        if char == "t" and temp is not None and len(temp) > 0:
            output += " CORE:" if names else " "
            # "acpitz" for ACPI Thermal Zone
            output += str(temp["coretemp"][0][1])
            output += "℉ " if fahrenheit else "℃ "

        if char == "f" and fans is not None and len(fans) > 0:
            output += " FAN:" if names else " "
            fan0 = next(iter(fans.values()))
            output += str(fan0[0][1]) + "/m "

        if char == 'm' and memory is not None:
            output += " MEM:" if names else " "
            output += str(round((memory[0] - memory[1]) / 1073741824, 1)) + "GB "

        if char == 'M' and memory is not None:
            output += " MEM:" if names else " "
            output += str(round((memory[3]) / 1073741824, 1)) + "/" + str(
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
            proc = "~" + proc
        string += proc + "% "
    return string


def freq_per_cpu(result):
    string = ""
    max_freq = 0
    for val in result:
        freq = str(round(val[0] / 1000, 1))
        string += freq + "|"
        max_freq = str(round(val[2] / 1000, 1))

    return string, max_freq


def graph_per_cpu(result):
    graph = "_▁▂▃▄▅▆▇███"

    string = ""
    for val in result:
        proc = int(round(val / 10, 0))
        string += graph[proc]
    return string


if __name__ == "__main__":
    main()
