#!/bin/sh

# cambiar la distribucion de teclado
setxkbmap dvorak

# Iniciar el compositor y la terminal
picom &
alacritty &

# Poner un fondo de pantalla
feh --bg-fill ~/Imagenes/108.jpeg

# Desactivar el apagado de pantalla por inactividad
xset s off s noblank -dpms

# Autoconfigurar las pantallas alineadas horizontalmente
xrandr --output LVDS1 --auto --primary --output HDMI1 --auto --pos $(xrandr | grep 'primary' | awk '{print $4}' | awk -F 'x' '{print $1}')x0
