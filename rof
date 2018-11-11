#!/bin/sh

# This script will launch the command given as an argument if not yet running
# Else it'll give focus to the command window

# Author: Piotr Miller
# e-mail: nwg.piotr@gmail.com
# Website: http://nwg.pl
# Project: https://github.com/nwg-piotr/tint2-executors
# License: GPL3

# Usage: rof [-P process_name] command

# Dependencies: `xorg-xprop`, `wmctrl`

if [[ $(which xprop) != *"/xprop"* ]]; then
    echo -e "\nDependencies: xorg-xprop package missing...\n"
    exit
fi
if [[ $(which wmctrl) != *"/wmctrl"* ]]; then
    echo -e "\nDependencies: wmctrl package missing...\n"
    exit
fi

if [ ! -z "$1" ]; then

    if [[ "$1" == "-P" ]]; then

       if [ "$#" -ge 3 ]; then
           # find process ID
           pid=$(xprop -name $2 | grep PID | awk '{print $3}')
           if [ ! -z "$pid" ]; then
               # find window ID by process ID
               win=$(wmctrl -lp | grep $pid | awk '{print $1}')
               wmctrl -i -a ${win}
           else
               sh -c "${@:3} &"
           fi
       else
           echo -e "\nShould be: rof -P process_name command\n"
       fi

    elif [[ "$1" == *"-h"* ]] || [[ "$1" == *"--help"* ]]; then
       echo -e "\nThis script [r]uns a command [o]r sets [f]ocus to its window if command is already running. May be used in two ways:\n"
       echo -e "1: \`rof command\` (e.g. \`rof tint2conf\`)\n"
       echo -e "- the command and the process name are the same;\n"
       echo -e "2: \`rof -P process_name command\` (e.g. \`rof -P zenity zenity-set-volume.sh\`)\n"
       echo -e "- where \`zenity-set-volume.sh\` is a script which launches \`zenity\` box with arguments.\n"


    else

       # find process ID
       pid=$(xprop -name $1 | grep PID | awk '{print $3}')
       if [ ! -z "$pid" ]; then
           # find window ID by process ID
           win=$(wmctrl -lp | grep ${pid} | awk '{print $1}')
           # "Set focus on window id $win"
           wmctrl -i -a ${win}
       else
           # "Launch a new instance of $1"
           sh -c "$@ &"
       fi
    fi
else
    echo -e "\nUsage: rof [-P process_name] command\n"
fi