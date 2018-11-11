#!/bin/sh

# Set the volume level with a zenity dialog box

# Dependencies: `alsa-utils`, `zenity`

lvl=$(amixer sget Master | grep 'Right:' | awk -F'[][]' '{ print $2 }')
lvl=${lvl::-1}
lvl=$(zenity --scale --value ${lvl} --title "Volume" --text "Set master volume level")
amixer sset 'Master' ${lvl}% -q
