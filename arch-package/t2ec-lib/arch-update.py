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

Arguments [-C<aur_helper>] | [-U<aur_helper> <terminal>] | [-N] | [-M<custom_name>] |-[O]

[-C<aur_helper>] - check updates
[-U<terminal>,<aur_helper>] - your AUR helper name
[-O] - show pending updates as notification
[-N] - name instead of icon


Dependencies: `pacman-contrib`
Optional: `pacaur` | `trizen` | `yay`
"""

import sys
import os
import subprocess


def main():
    name = None
    helper_name, terminal_name, helper_cmd, updates = "", "", "", ""
    do_check, do_update, do_notify = False, False, False

    tmp_file = os.getenv("HOME") + "/.arch-updates"

    check_command = 'sh -c "checkupdates > ' + tmp_file

    aur_check_commands = {'pacaur': 'pacaur check -q',
                          'trizen': 'trizen -Qqu -a',
                          'yay': 'yay -Qqu -a'}

    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):

            if sys.argv[i].upper() == '-O':
                do_check = False
                do_update = False
                do_notify = True
                break

            if sys.argv[i].upper().startswith('-C'):
                try:
                    helper_cmd = aur_check_commands[sys.argv[i][2::]]
                except KeyError:
                    helper_cmd = ""
                    pass
                if helper_cmd:
                    check_command += " && " + helper_cmd
                check_command += ' >> ' + tmp_file + '"'
                do_check = True
                do_update = False
                do_notify = False

            if sys.argv[i].upper().startswith('-U'):
                tools = sys.argv[i][2::].split(":")
                terminal_name = tools[0]
                try:
                    helper_name = tools[1]
                except IndexError:
                    helper_name = "sudo pacman"
                do_check = False
                do_update = True
                do_notify = False

            if sys.argv[i].upper() == '-N':
                name = "Upd:"

            if sys.argv[i].upper().startswith('-M'):
                name = sys.argv[i][2::]

            if sys.argv[i].upper() == '-H' or sys.argv[i].upper() == '-HELP':
                print("\nt2ec --updates -C[aur_helper] | -U<terminal>[:aur_helper] | [-O] [-N] | [-M<custom_name>]\n")
                print("-C[aur_helper] - (C)heck updates with pacman and optionally AUR helper")
                print(" example: t2ec --update -Ctrizen\n")
                print("-U<terminal>[:aur_helper] - (U)pdate in <terminal> with pacman or AUR helper")
                print(" example: t2ec --update -Uxfce4-terminal:trizen\n")
                print("-O - display saved pending updates as n(O)tification")
                print("-N - print (N)ame instead of icon")
                print("-M<custom_name> - print custom na(M)e instead of icon\n")

    if do_check:
        subprocess.call(check_command, shell=True)
        updates = open(tmp_file, 'r').read().rstrip()
        num_upd = len(updates.splitlines())

        if name is not None:
            print(name + " " + str(num_upd))
        else:
            if num_upd > 0:
                print("/usr/share/t2ec/arch-icon-notify.svg")
                print(num_upd)
            else:
                print("/usr/share/t2ec/arch-icon.svg")

        if num_upd > 0:
            notify(updates)

    if do_update:
        command = terminal_name + ' -e \'sh -c \"' + helper_name + ' -Syu; echo Press enter to exit; read; killall -SIGUSR1 tint2\"\''
        subprocess.call(command, shell=True)

    if do_notify:
        updates = open(tmp_file, 'r').read().rstrip()
        notify(updates)


def notify(updates):
    subprocess.call(
        ['notify-send', "Pending updates:", "--icon=/usr/share/t2ec/arch-update48.svg", "--expire-time=5000", updates])


if __name__ == "__main__":
    main()
