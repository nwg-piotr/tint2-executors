#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
Development in progress.

Dependencies: wget
"""

import subprocess
import json
from collections import namedtuple
import locale
import os
import sys
import re


def main():
    t2ec_dir = os.getenv("HOME") + "/.t2ecol"
    response = None
    name = None
    img_path = "~/PycharmProjects/tint2-executors/images/"  # todo change to /usr/share/t2ec/

    settings = Settings()

    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            if sys.argv[i].upper() == '-N':
                name = "Weather:"

            if sys.argv[i].upper().startswith('-M'):
                name = sys.argv[i][2::]

            if sys.argv[i].startswith("-I"):
                settings.items = sys.argv[i][2::]

            if sys.argv[i].startswith("-A"):
                settings.api_key = sys.argv[i][2::]

            if sys.argv[i].startswith("-C"):
                settings.city_id = sys.argv[i][2::]

            if sys.argv[i].startswith("-U"):
                settings.units = sys.argv[i][2::]

            if sys.argv[i].startswith("-L"):
                settings.lang = sys.argv[i][2::]

    if settings.img_path is not None:
        img_path = settings.img_path

    if name is not None:
        os.system("echo Checking...")
    else:
        os.system("echo /usr/share/t2ec/refresh.svg")
        os.system("echo ''")

    request_url = "http://api.openweathermap.org/data/2.5/weather?id=" + settings.city_id + "&appid=" + \
                  settings.api_key + "&units=" + settings.units + "&lang=" + settings.lang
    try:
        response = subprocess.check_output("wget -qO- '" + request_url + "'", shell=True)
        subprocess.call(["echo '" + str(response) + "' > " + t2ec_dir + "/.weather-" + settings.city_id], shell=True)

    except subprocess.CalledProcessError as exitcode:
        if name is None:
            os.system("echo /usr/share/t2ec/refresh.svg")
        os.system("echo Exit code: " + str(exitcode.returncode))
        exit(0)

    if response is not None:
        # Convert JSON to object - after DS. at https://stackoverflow.com/a/15882054/4040598
        owm = json.loads(response, object_hook=lambda d: namedtuple('t', d.keys())(*d.values()))
        print_output(owm, name, settings.items, settings.units, img_path)


def print_output(owm, name, items, units, img_path):
    icons = {'01d': 'ow-01d.png',
             '01n': 'ow-01n.png',
             '02d': 'ow-02d.png',
             '02n': 'ow-02n.png',
             '03d': 'ow-03d.png',
             '03n': 'ow-03d.png',
             '04d': 'ow-04d.png',
             '04n': 'ow-04d.png',
             '09d': 'ow-09d.png',
             '09n': 'ow-09d.png',
             '10d': 'ow-10d.png',
             '10n': 'ow-10n.png',
             '11d': 'ow-11d.png',
             '11n': 'ow-11d.png',
             '13d': 'ow-13d.png',
             '13n': 'ow-13d.png',
             '50d': 'ow-50d.png',
             '50n': 'ow-50d.png'}

    if owm.cod == 200:
        #print(owm)
        # Prepare items
        icon = "images/refresh.svg"
        try:
            icon = img_path + icons[str(getattr(owm.weather[0], "icon"))]
        except KeyError:
            pass

        city = str(owm.name + ", " + getattr(owm.sys, "country"))

        s_desc = str(getattr(owm.weather[0], "main"))

        desc = str(getattr(owm.weather[0], "description"))

        unit = "℉" if units == "imperial" else "℃"
        temp = str(round(float(str(getattr(owm.main, "temp"))), 1)) + unit

        pressure = str(int(round(float(str(getattr(owm.main, "pressure"))), 0))) + " hpa"

        humidity = str(round(float(str(getattr(owm.main, "humidity"))), 0)) + "%"

        unit = "m/h" if units == "imperial" else "m/s"
        wind = str(getattr(owm.wind, "speed")) + " " + unit + ", " + wind_dir(float(str(getattr(owm.wind, "deg"))))

        output = ""
        if name is None:
            os.system("echo " + icon)
        else:
            output += name

        for i in range(len(items)):
            if items[i] == "c":
                output += " " + city + " "
            if items[i] == "s":
                output += " " + s_desc + " "
            if items[i] == "d":
                output += " " + desc + " "
            if items[i] == "t":
                output += " " + temp + " "
            if items[i] == "p":
                output += " " + pressure + " "
            if items[i] == "h":
                output += " " + humidity + " "
            if items[i] == "w":
                output += " " + wind + " "

        print(re.sub(' +', ' ', output).strip())

    else:
        if name is None:
            os.system("echo /usr/share/t2ec/refresh.svg")
        os.system("echo HTTP status: " + str(owm.cod))
        exit(0)


class Settings:
    def __init__(self):
        super().__init__()

        t2ec_dir = os.getenv("HOME") + "/.t2ecol"
        # Create settings file if not found
        if not os.path.isdir(t2ec_dir):
            os.makedirs(t2ec_dir)
        if not os.path.isfile(t2ec_dir + "/weatherrc"):
            config = [
                "# Items: [s]hort description, [d]escription, [t]emperature, [p]ressure, [h]umidity, [w]ind, [c]ity name\n",
                "# API key: go to http://openweathermap.org and get one\n",
                "# city_id you will find at http://openweathermap.org/find\n",
                "# units may be metric or imperial\n",
                "# Uncomment lang to override system $LANG value\n",
                "# Uncomment img_path to override built-in icons\n",
                "# \n",
                "# Delete this file if something goes wrong :)\n",
                "# ------------------------------------------------\n",
                "items = tpw\n",
                "api_key = your_key_here\n",
                "city_id = 2643743\n",
                "units = metric\n",
                "#lang = en\n",
                "#img_path = /home/user/my_custom_icons/"]

            subprocess.call(["echo '" + ''.join(config) + "' > " + t2ec_dir + "/weatherrc"], shell=True)

        self.items = "tpw"
        self.api_key = ""
        self.city_id = "2643743"  # London, UK
        self.units = "metric"
        self.lang = None
        self.img_path = None

        # read from settings file
        lines = open(t2ec_dir + "/weatherrc", 'r').read().rstrip().splitlines()

        for line in lines:
            if not line.startswith("#"):
                if line.startswith("items"):
                    self.items = line.split("=")[1].strip()
                elif line.startswith("api_key"):
                    self.api_key = line.split("=")[1].strip()
                elif line.startswith("city_id"):
                    self.city_id = line.split("=")[1].strip()
                elif line.startswith("units"):
                    self.units = line.split("=")[1].strip()
                elif line.startswith("lang"):
                    self.lang = line.split("=")[1].strip()
                elif line.startswith("img_path"):
                    self.img_path = line.split("=")[1].strip()

        if self.lang is None:
            loc = locale.getdefaultlocale()[0][:2]
            self.lang = loc if loc else "en"


def wind_dir(deg):
    if deg >= 348.75 or deg <= 11.25:
        return "N"
    elif 11.25 < deg <= 33.75:
        return "NNE"
    elif 33.75 < deg <= 56.25:
        return "NE"
    elif 56.25 < deg <= 78.75:
        return "ENE"
    elif 78.75 < deg <= 101.25:
        return "E"
    elif 101.25 < deg <= 123.75:
        return "ESE"
    elif 123.75 < deg <= 146.25:
        return "SE"
    elif 146.25 < deg <= 168.75:
        return "SSE"
    elif 168.75 < deg <= 191.25:
        return "S"
    elif 191.25 < deg <= 213.75:
        return "SSW"
    elif 213.75 < deg <= 236.25:
        return "SW"
    elif 236.25 < deg <= 258.75:
        return "WSW"
    elif 258.75 < deg <= 281.25:
        return "W"
    elif 281.25 < deg <= 303.75:
        return "WNW"
    elif 303.75 < deg <= 326.25:
        return "NW"
    elif 326.25 < deg <= 348.75:
        return "NNW"
    else:
        return "WTF"



if __name__ == "__main__":
    main()
