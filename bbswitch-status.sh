#!/bin/bash

bb_status=$(cat /proc/acpi/bbswitch | awk -F ' ' '{print $2}')

if [ "$bb_status" = "ON" ]; then
  echo images/nvidia.svg
fi