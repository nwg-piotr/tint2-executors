# Tint2 executors collection
I thought to publish my collection of executors for [Tint2](https://gitlab.com/o9000/tint2) panel here, in hope it's useful to someone. Some of the scripts are only
useful on [Arch Linux](https://www.archlinux.org), but most part should work anywhere. Let's start from the latest one:

## [cpu-fan-memory.py](cpu-fan-memory.py)
This script uses the `python-psutil` module to display the CPU average load, frequency (current/max),
the temperature sensor reading, the fan speed and memory usage (used/total).

![cpu-fan-memory overview](http://nwg.pl/wiki-tint2-executors/cpu-fan-memory-overview.png)

![cpu-fan-memory zoom](http://nwg.pl/wiki-tint2-executors/cpu-fan-memory-zoom.png)

**Command:** `python ~/tint2-executors/cpu-fan-memory.py [-options]`

[Wiki: -options, sample executor](https://github.com/nwg-piotr/tint2-executors/wiki/CPU-load,-fan-speed,-memory-usage)

## [bbswitch-status.sh](https://github.com/nwg-piotr/tint2-executors/blob/master/bbswitch-status.sh)

Have you ever needed to know if your hybrid (Optimus) laptop is currently running Intel or Nvidia graphics? In GNOME [there was an extension for that](https://extensions.gnome.org/extension/1100/bumblebee-status). Out of boredom I took a look at its code, which resulted in this short script.

![bbswitch-status](http://nwg.pl/wiki-tint2-executors/bumblebee-status.png)

**Command:** `~/tint2-executors/bbswitch-status.sh`

[Wiki: sample executor](https://github.com/nwg-piotr/tint2-executors/wiki/Bumblebee-status)

## [speedtest.sh](https://github.com/nwg-piotr/tint2-executors/blob/master/speedtest.sh)

Lately I needed to pfoor that my Internet connection sucks. And not as fast as the provider claims it does. To collect data on the speed over time, I used this bash script in a Tint2 executor. It saves Ping [ms] Download and Upload speed [Mbit/s] every a certain interval to ~/speedtest.txt.

## more scripts 
Coming soon.

# Installation (all-in-one):

Clone the repository to your home directory:

`$ git clone https://github.com/nwg-piotr/tint2-executors.git`

Check [Wiki](https://github.com/nwg-piotr/tint2-executors/wiki) for sample Tint2 executors.
