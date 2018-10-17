# tint2-executors
I thought to publish my collection of executors for Tint2 panel here, in hope it's useful to someone. Some of them are only
useful on [Arch Linux](https://www.archlinux.org), the others may be used anywhere. Let's start from the latest one:

## [cpu-fan-memory.py](cpu-fan-memory.py)
This script uses the `python-psutil` module to display the CPU average load, frequency (current/max),
the temperature sensor reading, the fan speed and memory usage (used/total).

![cpu-fan-memory overview](http://nwg.pl/wiki-tint2-executors/cpu-fan-memory-overview.png)

![cpu-fan-memory zoom](http://nwg.pl/wiki-tint2-executors/cpu-fan-memory-zoom.png)

**Command:** `python ~/tint2-executors/cpu-fan-memory.py [-options]`

[More on Wiki](https://github.com/nwg-piotr/tint2-executors/wiki/CPU-load,-fan-speed,-memory-usage)

## [bbswitch-status.sh](https://github.com/nwg-piotr/tint2-executors/blob/master/bbswitch-status.sh)

![bbswitch-status](http://nwg.pl/wiki-tint2-executors/bumblebee-status.png)

Have you ever needed to know if your hybrid (Optimus) laptop is currently running Intel or Nvidia graphics? In GNOME [there was an extension for that](https://extensions.gnome.org/extension/1100/bumblebee-status). Out of boredom I took a look at its code, which resulted in this short script.

**Command:** `~/tint2-executors/bbswitch-status.sh`

## more scripts coming soon...

# Installation:

Clone the repository to your home directory:

`$ git clone https://github.com/nwg-piotr/tint2-executors.git`

