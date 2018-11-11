# Tint2 executors collection
While playing with Openbox, we often need a script to perform some actions not included OOTB. Having to search the same answers again and again on each new machine, I thought it was worth documenting them somewhere for further use.

The [Tint2 panel](https://gitlab.com/o9000/tint2) - a brilliant and flexible piece of software - allows to execute scripts every certain period of time. At least some of these scripts should also be useful in other applications (panels?), however.

If you find the project useful, feel free to contribute. Many thanks to [PackRat](https://github.com/PackRat-SC2018), [Head_on_a_Stick](https://forum.archlabslinux.com/u/head_on_a_stick/summary), [Nathaniel](https://github.com/natemaia) for advices and pull requests.

## [cpu-fan-mem.py](https://github.com/nwg-piotr/tint2-executors/blob/master/cpu-fan-mem.py)
This script uses the `python-psutil` module to display the CPU load (graph or percentage per core or average percentage), frequency (current/max), the temperature sensor reading, the fan speed and memory usage (used/total).

![cpu-fan-mem](http://nwg.pl/wiki-tint2-executors/cpu-fan-mem.png)

**Command:** `python ~/tint2-executors/cpu-fan-mem.py [-C{components}] [-F] [-T]`

[Wiki: options, sample executor](https://github.com/nwg-piotr/tint2-executors/wiki/CPU-load,-temperature,-fan-speed,-memory-usage)

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

This script has mainly aesthetic values: it should rather be used next to the built-in Tint2 battery indicator, not instead of it. It displays an appropriate battery icon, according to the current charge level and charging state.

![battery icon](http://nwg.pl/wiki-tint2-executors/battery-icon.png)

**Command:** `~/tint2-executors/battery-icon.sh`

[Wiki: dependencies, sample executor](https://github.com/nwg-piotr/tint2-executors/wiki/Battery-icon)

## [desktop.py](https://github.com/nwg-piotr/tint2-executors/blob/master/desktop.py)

This Python script displays current desktop indicator. It also allows to switch desktops.

![desktop icon](http://nwg.pl/wiki-tint2-executors/desktop-icon.png)

[Wiki: dependencies, optional arguments, sample executor](https://github.com/nwg-piotr/tint2-executors/wiki/Desktop-indicator-and-switcher)

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

## [arch-update.sh](https://github.com/nwg-piotr/tint2-executors/blob/master/arch-update.sh)

This script displays an icon to indicate Arch / AUR package updates available. Likely to need some customization to work well on each machine, as it depends on the terminal and AUR helper you use. Check [Wiki](https://github.com/nwg-piotr/tint2-executors/wiki/Arch-update-notifier) for details.

![Arch update notifier](http://nwg.pl/wiki-tint2-executors/arch-update.png)

**Command:** ~/tint2-executors/./arch-update.sh

[Wiki: dependencies, customization, sample executor](https://github.com/nwg-piotr/tint2-executors/wiki/Arch-update-notifier)

# Installation (all-in-one):

Clone the repository to your home directory:

`$ git clone https://github.com/nwg-piotr/tint2-executors.git`

To install all dependencies in one step, you may use the [tint2-executors](https://github.com/nwg-piotr/tint2-executors/raw/master/tint2-executors-0.0.1-1-x86_64.pkg.tar.xz) dummy package. **Attention: just added, not yet really tested, so some dependencies may still be missing.**

Check [Wiki](https://github.com/nwg-piotr/tint2-executors/wiki) for more details and sample Tint2 executors.
