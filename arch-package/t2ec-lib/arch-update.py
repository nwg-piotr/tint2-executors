#!/usr/bin/python
# _*_ coding: utf-8 _*_

"""
# Author: Piotr Miller
# e-mail: nwg.piotr@gmail.com
# Website: http://nwg.pl
# Project: https://github.com/nwg-piotr/tint2-executors
# License: GPL3

# Credits: RaphaelRochet/arch-update
# https://github.com/RaphaelRochet/arch-update
# Icon by @edskeye

Arguments -T<terminal> [-A<aur_helper>] | [-C] | [-U] | [-N]

-T<terminal> - your terminal name
[-U<aur_helper>] - your AUR helper name
[-C] - check updates
[-N] - name instead of icon

Dependencies: `pacman-contrib`
Optional: `pacaur` | `trizen` | `yay`
"""

import sys
import os
import subprocess


def main():
    terminal, aur_helper, updates = None, None, None
    helper = ""
    check_updates, update, display_name = False, False, False

    tmp_file = os.getenv("HOME") + "/arch-updates"
    check_command = 'sh -c "/usr/bin/checkupdates'

    aur_check_commands = {'pacaur': 'pacaur -Qqu -a', 'trizen': 'trizen -Qqu -a', 'yay': 'yay -Qqu'}

    aur_update_commands = {'pacaur': 'sh -c "pacaur -Syu ; echo Done - Press enter to exit; read"',
                          'trizen': 'trizen -Syu ; echo Done - Press enter to exit; read',
                          'yay': 'sh -c "yay ; echo Done - Press enter to exit; read"'}

    for i in range(1, len(sys.argv)):

        if sys.argv[i].upper().startswith("-T"):
            terminal = sys.argv[i][2::]

        if sys.argv[i].upper().startswith("-A"):
            try:
                helper = aur_check_commands[sys.argv[i][2::]]
            except KeyError:
                pass
            if helper:
                check_command += ' && ' + helper
            check_command += '" > ' + tmp_file

        if sys.argv[i].upper() == "-C":
            check_updates = True

        if sys.argv[i].upper() == "-N":
            display_name = True

    os.system(check_command)
    updates = open(tmp_file, 'r').read().rstrip()
    #os.remove(tmp_file)
    print(updates)
    num_upd = len(updates.splitlines())
    subprocess.call(['notify-send', "Pending updates:", "--icon=/usr/share/t2ec/bat-empty.svg", "--expire-time=5000", updates])


if __name__ == "__main__":
    main()
