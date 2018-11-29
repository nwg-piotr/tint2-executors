# t2ec package (AUR)

To simplify installation and usage of the scripts which are not a part of the [psuinfo](https://github.com/nwg-piotr/psuinfo) package, I thought to give them a PKGBUILD file, and a common command, too:

```bash
t2ec --script [argument]
```

##Example:

`t2ec --volume` - to draw the volume icon + current volume level

`t2ec --volume -N` - to print "Vol: " + current volume level

`t2ec --volume [up] | [down] | [toggle] | [level]` - to use as mouse event commands

Together with the [psuinfo](https://github.com/nwg-piotr/psuinfo) package, all the most useful scripts are now unified and given common syntax:

![scripts in action](http://nwg.pl/wiki-tint2-executors/my-panels-261118.jpg)

##Installation:

Please install the [t2ec (AUR) package](https://aur.archlinux.org/packages/t2ec).

For `psuinfo` commands install the [psuinfo (AUR) package](https://aur.archlinux.org/packages/psuinfo).

##Commands to display information
 
`[-N]` replaces icons with text:

`t2ec --desktop [-N]`

`t2ec --bbswitch [-N]`

`t2ec --volume [-N]`

`t2ec --brightness [-N]`

`t2ec --lbrightness [-N]` (for `light-git` optional package)

`t2ec --battery [-l] | [-N]` (`[-l]` for icon + level, `[-N]` for "Bri: " + level

`t2ec --wifi [-N] | [-M'custom name']`

`t2ec --update -C[aur_helper] [-N] | [-M<custom_name]`

##Commands to assign to mouse events:

`t2ec --desktop [next] | [prev] | [<number>]`

`t2ec --volume [up] | [down] | [<level>]`

`t2ec --brightness [up] | [down] | [<level>]`

`t2ec --lbrightness [up] | [down] | [<level>]` (for 'light-git' optional package)

`t2ec --update -U<terminal>[:aur_helper]`

`t2ec --update -O` displays n(O)tifiction with the last saved updates list


*Remember to uncheck 'Show icon' in executor if textual display selected!*

##Menus:

`t2ec --command menu` - assigned to a mouse event (preferrably left/right click) allows to attach context menus to executors.

You need the [jgmenu](https://github.com/johanmalm/jgmenu) package (optional dependency) installed and initialized (`jgmenu init`).

Two of the commands have predefined menus: `t2ec --update menu` and `t2ec --desktop menu` will display:

![predefined menus](http://nwg.pl/wiki-tint2-executors/t2ec-menus-predefined.png)

Other commands launched with the `menu` argument will use a sample template. All templates are being
created in the `~/.t2ecol` hidden folder as soon, as you run the command for the first time.
You may customize templates to your taste. To restore defaults, just remove the modified template.

Check the [jgmenu reference document](https://github.com/johanmalm/jgmenu/blob/master/docs/manual/jgmenu.1.md) to learn more.

##Helper command:

`t2ec --zbox [bri] | [vol]` - displays Zenity box to set volume | brightness level. Depends on 'zenity' and 'rof-git' optional packages.

**Sample usage in Tint2**:

![sample executor](http://nwg.pl/wiki-tint2-executors/tint2conf-commented.png)
