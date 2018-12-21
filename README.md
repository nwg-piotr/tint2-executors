# Tint2 executors collection
While playing with Openbox, we often need a script to perform some actions not included OOTB. Having to search the same answers again and again on each new machine, I thought it was worth documenting them somewhere for further use.

The [Tint2 panel](https://gitlab.com/o9000/tint2) - a brilliant and flexible piece of software - allows to execute scripts every certain period of time. At least some of these scripts should also be useful in other applications (panels?).

This repository contains scripts of various usability in various stages of development. Always up to date versions you'll find in separate repositories:

## [psuinfo](https://github.com/nwg-piotr/psuinfo) 

Contains a python-psutil-based script, which provides a set of commands to display information on system resources usage. In Tint2 panel you may choose from graphical (icons) and textual format. Published as [psuinfo](https://aur.archlinux.org/packages/psuinfo) (AUR) package for Arch Linux and in official Void Linux repository.

## [t2ec](https://github.com/nwg-piotr/t2ec)

Contains the rest of most useful scripts, which as well display system info, as allow to assign some useful actions to mouse clicks: desktop indicator/switcher, Bumblebee status, brightness and volume level, wi-fi network in use, Arch updates and current weather. [AUR](https://aur.archlinux.org/packages/t2ec)

## [rof](https://github.com/nwg-piotr/rof)

A simple helper script, which is a launcher allowing to avoid running multiple instances of the same window. Useful while assigning commands to mouse click event. [AUR](https://aur.archlinux.org/packages/rof-git)

## Sample usage:

![scripts in action](http://nwg.pl/wiki-tint2-executors/my-panels-201218.jpg)

___
**Attention: all the content described below this point concerns development versions, which may not contain latest changes. Use of packages named above is strongly recommended.**
___

## [bbswitch-status-temp.sh](https://github.com/nwg-piotr/tint2-executors/blob/master/bbswitch-status-temp.sh)

Displays an icon according to the current Bumblebee status. If NVIDIA graphics turned on, it'll also display the GPU temperature.

![bbswitch-status-temperature](http://nwg.pl/wiki-tint2-executors/icon-bbswitch-status-temp.png)

**Command:** `~/tint2-executors/bbswitch-status-temp.sh`

[Wiki: dependencies, sample executor](https://github.com/nwg-piotr/tint2-executors/wiki/Bumblebee-status)

## [brightness-icon.sh](https://github.com/nwg-piotr/tint2-executors/blob/master/brightness-icon.sh)

This script displays an appropriate brightness icon, according to the current brightness level. Assign scroll up/down  command to increase/decrease level. Use `-l` argument to display level as text next to the icon.

![brightness icon](http://nwg.pl/wiki-tint2-executors/icon-brightness.png)

**Command:** `~/tint2-executors/brightness-icon.sh`

[Wiki: dependencies, sample executor](https://github.com/nwg-piotr/tint2-executors/wiki/Brightness-icon)

## [volume-icon.sh](https://github.com/nwg-piotr/tint2-executors/blob/master/volume-icon.sh)

This script displays an appropriate volume icon, according to the current volume level. Assign scroll up/down command to increase/decrease level. Use `-l` argument to display level as text next to the icon.

![volume icon](http://nwg.pl/wiki-tint2-executors/icon-volume.png)

**Command:** `~/tint2-executors/volume-icon.sh`

[Wiki: dependencies, sample executor](https://github.com/nwg-piotr/tint2-executors/wiki/Volume-icon)

## [battery-icon.sh](https://github.com/nwg-piotr/tint2-executors/blob/master/battery-icon.sh)

This script displays an appropriate battery icon, according to the current charge level and charging state. It has mainly aesthetic values: it should rather be used next to the built-in Tint2 battery indicator, not instead of it. However, you may use `-l` argument to display level as text next to the icon.

![battery icon](http://nwg.pl/wiki-tint2-executors/icon-battery.png)

**Command:** `~/tint2-executors/battery-icon.sh`

[Wiki: dependencies, sample executor](https://github.com/nwg-piotr/tint2-executors/wiki/Battery-icon)

## [desktop.py](https://github.com/nwg-piotr/tint2-executors/blob/master/desktop.py)

This Python script displays current desktop indicator. Assign scroll up/down command with `n` | `p` (next | previous) argument to switch desktops.

![desktop icon](http://nwg.pl/wiki-tint2-executors/icon-desktop.png)

[Wiki: dependencies, optional arguments, sample executor](https://github.com/nwg-piotr/tint2-executors/wiki/Desktop-indicator-and-switcher)

## [wifi-name.sh](https://github.com/nwg-piotr/tint2-executors/blob/master/wifi-name.sh)

Bash script to display the name of Wi-Fi network currently in use, labeled with an icon or text.

![wi-fi name](http://nwg.pl/wiki-tint2-executors/wifi-name.png)

**Command:** `~/tint2-executors/wifi-name.sh`

[Wiki: optional agruments, sample executor](https://github.com/nwg-piotr/tint2-executors/wiki/Wi-Fi-networkname)

## [arch-update.sh](https://github.com/nwg-piotr/tint2-executors/blob/master/arch-update.sh)

This script displays an icon to indicate Arch / AUR package updates available. Likely to need some customization to work well on each machine, as it depends on the terminal and AUR helper you use. Check [Wiki](https://github.com/nwg-piotr/tint2-executors/wiki/Arch-update-notifier) for details.

![Arch update notifier](http://nwg.pl/wiki-tint2-executors/arch-update.png)

**Command:** ~/tint2-executors/./arch-update.sh

[Wiki: dependencies, customization, sample executor](https://github.com/nwg-piotr/tint2-executors/wiki/Arch-update-notifier)

## [zenity-set-brightness.sh](https://github.com/nwg-piotr/tint2-executors/blob/master/zenity-set-brightness.sh)

Opens a Zenity box to set the brightness level. Could be used e.g. as the left click action with the [brightness icon](https://github.com/nwg-piotr/tint2-executors/wiki/Brightness-icon).

![brightness zenity box](http://nwg.pl/wiki-tint2-executors/zenity-set-brightness.png)

**Command:** `~/tint2-executors/zenity-set-brightness.sh`

[Wiki: dependencies](https://github.com/nwg-piotr/tint2-executors/wiki/Brightness-zenity-box)

## [zenity-set-volume.sh](https://github.com/nwg-piotr/tint2-executors/blob/master/zenity-set-volume.sh)

Opens a Zenity box to set the volume level. Could be used e.g. as the left click action with the [volume icon](https://github.com/nwg-piotr/tint2-executors/wiki/Volume-icon).

![volume zenity box](http://nwg.pl/wiki-tint2-executors/zenity-set-volume.png)

**Command:** `~/tint2-executors/zenity-set-volume.sh`

[Wiki: dependencies](https://github.com/nwg-piotr/tint2-executors/wiki/Volume-zenity-box)

## [speedtest.sh](https://github.com/nwg-piotr/tint2-executors/blob/master/speedtest.sh)

Lately I needed to prove that my Internet connection sucks. And not as fast as the provider claims it does. To collect data on the speed over time, I used this bash script in a Tint2 executor. It saves Ping [ms] Download and Upload speed [Mbit/s] every a certain interval to ~/speedtest.txt.

![speedtest-cli >> txt](http://nwg.pl/wiki-tint2-executors/speedtest-cli-txt.png)

**Command:** `~/tint2-executors/speedtest.sh`

[Wiki: dependencies, sample executor and output](https://github.com/nwg-piotr/tint2-executors/wiki/speedtest.cli-to-speedtest.txt)

## [cpu-fan-mem.py](https://github.com/nwg-piotr/tint2-executors/blob/master/cpu-fan-mem.py) (deprecated)
___
**Important note:** the cpu-fan-mem.py script has been turned into a separate [project](https://github.com/nwg-piotr/psuinfo) and also [AUR package](https://aur.archlinux.org/packages/psuinfo), and will no longer be updated here. The description below, Wiki and the script itself are out of date. Please check the project site.
