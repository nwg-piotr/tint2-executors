#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
Development just started. Nothing useful inside yet.

Dependencies: wget
Items:
    S - Short description (main)
    D - Description (description)
    T - Temp [℃ | ℉]
    P - Pressure [hpa]
    H - Humidity [%]
    W - Wind [m/s, degrees]
    C - City name (name)
"""

import subprocess
import json
from collections import namedtuple
import locale
import os


def main():
    response = None
    settings = Settings()

    if settings.lang is None:
        loc = locale.getdefaultlocale()[0][:2]
        settings.lang = loc if loc else "en"

    print(settings.api_key)
    print(settings.city_id)
    print(settings.units)
    print(settings.lang)

    request_url = "http://api.openweathermap.org/data/2.5/weather?id=" + settings.city_id + "&appid=" + \
                  settings.api_key + "&units=" + settings.units + "&lang=" + settings.lang
    try:
        response = subprocess.check_output("wget -qO- '" + request_url + "'", shell=True)
    except subprocess.CalledProcessError as exitcode:
        print("Error accessing openweathermap.org, exit code: ", exitcode.returncode)
        exit(0)

    if response is not None:
        # after DS. at https://stackoverflow.com/a/15882054/4040598
        owm = json.loads(response, object_hook=lambda d: namedtuple('t', d.keys())(*d.values()))

        if owm.cod == 200:
            print(owm)
            print(owm.weather)
            print(getattr(owm.weather[0], "main"))
            print(getattr(owm.main, "temp"))

        else:
            print("Error accessing openweathermap.org, HTTP status: " + str(owm.cod))


class Settings:
    def __init__(self):
        super().__init__()

        t2ec_dir = os.getenv("HOME") + "/.t2ecol"
        # Create settings file if not found
        if not os.path.isdir(t2ec_dir):
            os.makedirs(t2ec_dir)
        if not os.path.isfile(t2ec_dir + "/weatherrc"):
            config = [
                "# Items: [S]hort description, [D]escription, [T]emperature, [P]ressure, [H]umidity, [W]ind, [C]ity name\n",
                "# API key: go to http://openweathermap.org and get one\n"
                "# units may be metric or imperial\n"
                "# uncomment lang to override system $LANG value\n"
                "# ------------------------------------------------\n"
                "items = CSTW\n",
                "api_key = your_key_here\n",
                "city_id = 2643743\n",
                "units = metric\n",
                "#lang = en"]

            subprocess.call(["echo '" + ''.join(config) + "' > " + t2ec_dir + "/weatherrc"], shell=True)

        self.api_key = ""
        self.city_id = "2643743"  # London, UK
        self.units = "metric"
        self.lang = None

        # read settings file
        lines = open(t2ec_dir + "/weatherrc", 'r').read().rstrip().splitlines()
        for line in lines:
            if not line.startswith("#"):
                if line.startswith("api_key"):
                    self.api_key = line.split("=")[1].strip()
                elif line.startswith("city_id"):
                    self.city_id = line.split("=")[1].strip()
                elif line.startswith("units"):
                    self.units = line.split("=")[1].strip()
                elif line.startswith("lang"):
                    self.lang = line.split("=")[1].strip()


if __name__ == "__main__":
    main()
