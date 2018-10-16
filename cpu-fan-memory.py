#!/usr/bin/env python

import sys
import psutil


def main():
    short = False

    if len(sys.argv) > 1:
        short = sys.argv[1] == "-S" or sys.argv[1] == "--short"

    # CPU load

    # Display load per CPU as semi-graph:
    print(graph_per_cpu(), end=" ")

    # Unhash a line below to choose a textual display instead of semi-graphical bar:

    # CPU average load:
    # print("CPU: " + str(psutil.cpu_percent(interval=1)), end = "% ")

    # Load per CPU as percentage:
    # print("CPU%: " + per_cpu(), end = " ")

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


def per_cpu():
    string = ""
    result = psutil.cpu_percent(interval=1, percpu=True)
    for val in result:
        proc = str(int(round(val, 1)))
        if len(proc) < 2:
            proc = "0" + proc
        string += proc + " "
    return string


def graph_per_cpu():

    # Unhash the pattern you like below or replace with your own:

    graph = "_▁▂▃▄▅▆▇███"
    # graph = " ⢀⣀⣠⣤⣴⣶⣾⣿⣿⣿"

    string = ""
    result = psutil.cpu_percent(interval=1, percpu=True)
    for val in result:
        proc = int(round(val / 10, 0))
        string += graph[proc]
    return string


if __name__ == "__main__":
    main()

