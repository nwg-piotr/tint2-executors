#!/usr/bin/env bash

# Set the brightness level with a zenity dialog box

# Dependencies: `xbacklight` or `light-git', `zenity`

# Prefer the `light` package, use `xbacklight` if `light` not found
if [[ $(which light) == *"/light"* ]]
then
    lvl=$(light -G)
else
    lvl=$(xbacklight -get)
fi

# Lets round the float result
lvl=$(echo "($lvl+0.5)/1" | bc)

lvl=$(zenity --scale --value ${lvl} --title "Brightness" --text "Set brightness level")

if [[ $(which light) == *"/light"* ]]
then
    light -S ${lvl}
else
    xbacklight -set ${lvl}
fi
