#!/bin/bash

bb_status=$(cat /proc/acpi/bbswitch | awk -F ' ' '{print $2}')

if [ "$bb_status" = "ON" ]; then
  echo ~/tint2-executors/images/nvidia.svg
fi