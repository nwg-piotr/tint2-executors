#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
Development just started. Nothing useful inside yet.

Dependencies: wget
Items:
    S - Short description (main)
    D - Description
    T - Temp [℃ | ℉]
    P - Pressure [hpa]
    H - Humidity [%]
    W - Wind [m/s, degrees]
    C - City name
"""

import subprocess
import json
from collections import namedtuple
import locale


def main():
    response = None
    # Defaults
    api_key = ""
    city_id = "2643743"  # London, UK
    units = "metric"
    lang = "en"

    # todo These values will later be read from preferences
    api_key = "f060ab40f2b012e72350f6acc413132a"
    city_id = "7532606"
    units = "metric"

    lang = locale.getdefaultlocale()[0][:2]

    request_url = "http://api.openweathermap.org/data/2.5/weather?id=" + city_id + "&appid=" + api_key + \
                  "&units=" + units + "&lang=" +lang
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

        else:
            print("Error accessing openweathermap.org, HTTP status: " + str(owm.cod))


if __name__ == "__main__":
    main()
