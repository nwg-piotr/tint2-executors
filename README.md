# tint2-executors
I thought to publish my collection of executors for Tint2 panel here, in hope it's useful to someone. Some of them are only
useful on [Arch Linux](https://www.archlinux.org), the others may be used anywhere.

Let's start from the latest one:

### [cpu-fan-memory.py](cpu-fan-memory.py)
This script uses the `python-psutil` module to display the CPU average load, frequency (current/max),
the temperature sensor reading, the fan speed and memory usage (used/total).

## Usage

1. `$ git clone https://github.com/nwg-piotr/tint2-executors.git`
2. Assuming you cloned to your home directory, add a Tint2 executor, enter path and command: `~/tint2-executors/command`, e.g. 
`~/tint2-executors/python cpu-fan-memory.py`. Change the path if you cloned to anywhere else. 
