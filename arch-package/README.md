To simplify installation of the scripts I like most, I thought to give them a PKGBUILD file, 
and a common command:

```bash
t2ec --script [argument]
```

**Example:**

`t2ec --volume` - to draw the volume icon + current volume level

`t2ec --volume -N` - to print "Vol: " + current volume level

`t2ec --volume [up] | [down] | [toggle] | [level]` - to use as mouse event commands

Together with the [psuinfo](https://github.com/nwg-piotr/psuinfo) package, all the most useful scripts (except for `arch-update.sh` at the moment) are now unified and given common syntax.

![commands map](http://nwg.pl/wiki-tint2-executors/my-panels-231118.png)
