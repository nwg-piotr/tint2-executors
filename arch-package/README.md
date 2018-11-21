To simplify installation of the scripts I like most, I thought to give them a PKGBUILD file, 
and a common command:

```bash
t2ec --script [argument]
```

Example: `t2ec --volume up`

This should simplify as well installation, as usage of the scripts in Tint2 executors significantly.

The installation process should perform following actions:

1. install necessary dependencies, propose optional dependencies
2. copy the `t2ec` command to /usr/bin
3. copy the scripts to /usr/lib/t2ec
4. copy all icons to /usr/share/t2ec

The scripts I'm currently thinking about:

![selection](http://nwg.pl/wiki-tint2-executors/package-selection.png)