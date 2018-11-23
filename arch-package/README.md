To simplify installation of the scripts I like most, I thought to give them a PKGBUILD file, 
and a common command:

```bash
t2ec --script [argument]
```

**Example:**

`t2ec --volume` - to draw the volume icon + current volume level

`t2ec --volume -N` - to print "Vol: " + current volume level

`t2ec --volume [up] | [down] | [toggle] | [level]` - to use as mouse event commands

Together with the [psuinfo](https://github.com/nwg-piotr/psuinfo) package, all the most useful scripts (except for `arch-update.sh` at the moment) are now unified and given common syntax:

![commands map](http://nwg.pl/wiki-tint2-executors/my-panels-231118.png)

The 0.1-7 package is in beta, and not yet published. You may find PKBUILD and the package above.

**Commands to display information** (`[-N]` replaces icons with text):

`t2ec --desktop [-N]`

`t2ec --bbswitch [-N]`

`t2ec --volume [-N]`

`t2ec --brightness [-N]`

`t2ec --lbrightness [-N]` (for `light-git` optional package)

`t2ec --battery [-l] | [-N]` (`[-l]` for icon + level, `[-N]` for "Bri: " + level

`t2ec --wifi [-N] | [-M'custom name']`

**Commands to assing to mouse events**:

`t2ec --desktop [next] | [prev] | [<number>]`

`t2ec --volume [up] | [down] | [<level>]`

`t2ec --brightness [up] | [down] | [<level>]`

`t2ec --lbrightness [up] | [down] | [<level>]` (for 'light-git' optional package)


*Remember to uncheck 'Show icon' in executor if textual display selected!*

**Helper command**:

`t2ec --zbox [bri] | [vol]` - displays Zenity box to set volume | brightness level. Depends on 'zenity' and 'rof-git' optional packages.
