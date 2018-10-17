# tint2-executors
I thought to publish my collection of executors for Tint2 panel here, in hope it's useful to someone. Some of them are only
useful on [Arch Linux](https://www.archlinux.org), the others may be used anywhere. Let's start from the latest one:

### [cpu-fan-memory.py](cpu-fan-memory.py)
This script uses the `python-psutil` module to display the CPU average load, frequency (current/max),
the temperature sensor reading, the fan speed and memory usage (used/total).

![cpu-fan-memory overview](http://nwg.pl/wiki-tint2-executors/cpu-fan-memory-overview.png)

![cpu-fan-memory zoom](http://nwg.pl/wiki-tint2-executors/cpu-fan-memory-zoom.png)

**Command:** `python ~/tint2-executors/cpu-fan-memory.py [-options]`

[More on Wiki](https://github.com/nwg-piotr/tint2-executors/wiki/CPU-load,-fan-speed,-memory-usage)

## Usage:

Clone the repository:

`$ git clone https://github.com/nwg-piotr/tint2-executors.git`

Assuming you cloned to your home directory, add a Tint2 executor, enter path and command, e.g.:

`~/tint2-executors/command`

Change the path if you cloned to anywhere else. 
