# Tint2 executors collection
I thought to publish my collection of executors for [Tint2](https://gitlab.com/o9000/tint2) panel here, in hope it's useful to someone. Some of the scripts are only
useful on [Arch Linux](https://www.archlinux.org), but most part should work anywhere

## [cpu-fan-memory.py](cpu-fan-memory.py)
This script uses the `python-psutil` module to display the CPU load (graph or percentage per core or average percentage), frequency (current/max), the temperature sensor reading, the fan speed and memory usage (used/total).

![cpu-fan-memory overview](http://nwg.pl/wiki-tint2-executors/cpu-fan-memory-overview.png)

![cpu-fan-memory zoom](http://nwg.pl/wiki-tint2-executors/cpu-fan-memory-zoom.png)

**Command:** `python ~/tint2-executors/cpu-fan-memory.py [-options]`

[Wiki: -options, sample executor](https://github.com/nwg-piotr/tint2-executors/wiki/CPU-load,-fan-speed,-memory-usage)

## [bbswitch-status.sh](https://github.com/nwg-piotr/tint2-executors/blob/master/bbswitch-status.sh)

Have you ever needed to know if your hybrid (Optimus) laptop is currently running Intel or Nvidia graphics? In GNOME [there was an extension for that](https://extensions.gnome.org/extension/1100/bumblebee-status). Out of boredom I took a look at its code, which resulted in this short script.

![bbswitch-status](http://nwg.pl/wiki-tint2-executors/bumblebee-status-on-off.png)

**Command:** `~/tint2-executors/bbswitch-status.sh`

[Wiki: sample executor](https://github.com/nwg-piotr/tint2-executors/wiki/Bumblebee-status)

## [bbswitch-status-temp.sh](https://github.com/nwg-piotr/tint2-executors/blob/master/bbswitch-status-temp.sh)

A variant of the script above. If NVIDIA graphics turned on, it displays approprate icon with the GPU temperature.

![bbswitch-status-temperature](http://nwg.pl/wiki-tint2-executors/bumblebee-status-temp.png)

**Command:** `~/tint2-executors/bbswitch-status-temp.sh`

[Wiki: dependencies, sample executor](https://github.com/nwg-piotr/tint2-executors/wiki/Bumblebee-status)

## [speedtest.sh](https://github.com/nwg-piotr/tint2-executors/blob/master/speedtest.sh)

Lately I needed to prove that my Internet connection sucks. And not as fast as the provider claims it does. To collect data on the speed over time, I used this bash script in a Tint2 executor. It saves Ping [ms] Download and Upload speed [Mbit/s] every a certain interval to ~/speedtest.txt.

![speedtest-cli >> txt](http://nwg.pl/wiki-tint2-executors/speedtest-cli-txt.png)

**Command:** `~/tint2-executors/speedtest.sh`

[Wiki: dependencies, sample executor and output](https://github.com/nwg-piotr/tint2-executors/wiki/speedtest.cli-to-speedtest.txt)

## [brightness-volume-level.sh](https://github.com/nwg-piotr/tint2-executors/blob/master/brightness-volume-level.sh)

This script displays current brightness and volume level.

![brightness and volume level](http://nwg.pl/wiki-tint2-executors/brightness-volume-level.png)

The [brightness-volume-inline.sh](https://github.com/nwg-piotr/tint2-executors/blob/master/brightness-volume-inline.sh) displays the values in a row.

![brightness and volume inline](http://nwg.pl/wiki-tint2-executors/brightness-volume-inline.png)

**Command:** `~/tint2-executors/./brightness-volume-level.sh` or `~/tint2-executors/./brightness-volume-inline.sh`

[Wiki: dependencies, sample executor](https://github.com/nwg-piotr/tint2-executors/wiki/Brightness-and-volume-level)

## [brightness-icon.sh](https://github.com/nwg-piotr/tint2-executors/blob/master/brightness-icon.sh)

This script displays an appropriate brightness icon, according to the current brightness level. By assigning left/right click command you may decrease/increase the level.

![brightness icon](http://nwg.pl/wiki-tint2-executors/brightness-icon1.png)

**Command:** `~/tint2-executors/brightness-icon.sh`

[Wiki: dependencies, sample executor](https://github.com/nwg-piotr/tint2-executors/wiki/Brightness-icon)

## [volume-icon.sh](https://github.com/nwg-piotr/tint2-executors/blob/master/volume-icon.sh)

This script displays an appropriate volume icon, according to the current volume level. Assigning left | middle | right click command to decrease | mute | increase the volume level.

![volume icon](http://nwg.pl/wiki-tint2-executors/volume-icon.png)

**Command:** `~/tint2-executors/volume-icon.sh`

[Wiki: dependencies, sample executor](https://github.com/nwg-piotr/tint2-executors/wiki/Volume-icon)

## [battery-icon.sh](https://github.com/nwg-piotr/tint2-executors/blob/master/battery-icon.sh)

This script has mainly aesthetic values: it should rather be used next to the built-in Tint2 battery indicator, not instead of it. It displays an appropriate battery icon, according to the current load level and charging state.

![volume icon](http://nwg.pl/wiki-tint2-executors/battery-icon.png)

**Command:** `~/tint2-executors/battery-icon.sh`

## [arch-update.sh](https://github.com/nwg-piotr/tint2-executors/blob/master/arch-update.sh)

This script displays an icon to indicate Arch / AUR package updates available. Likely to need some customization to work well on each machine, as it depends on the terminal and AUR helper you use. Check [Wiki](https://github.com/nwg-piotr/tint2-executors/wiki/Arch-update-notifier) for details.

![Arch update notifier](http://nwg.pl/wiki-tint2-executors/arch-update.png)

**Command:** ~/tint2-executors/./arch-update.sh

[Wiki: dependencies, customization, sample executor](https://github.com/nwg-piotr/tint2-executors/wiki/Arch-update-notifier)

# Installation (all-in-one):

Clone the repository to your home directory:

`$ git clone https://github.com/nwg-piotr/tint2-executors.git`

Check [Wiki](https://github.com/nwg-piotr/tint2-executors/wiki) for more details and sample Tint2 executors.
