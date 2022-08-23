#!/bin/sh

# Background image restore.
#------------------------------------
nitrogen --restore &
picom &

# Keyboard en_US layout.
#------------------------------------
setxkbmap us &

# Resolution configuration.
#------------------------------------
#xrandr --output Virtual1 --primary --mode 2560x1440 --pos 0x0 

# System Icons.
#------------------------------------
udiskie -t &

# Network Manager Applet.
#------------------------------------
nm-applet &

# Volume icon GUI interaction.
#------------------------------------
volumeicon &

cbatticon -u 5 &
