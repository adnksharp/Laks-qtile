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

# Autoconfigurar las pantallas
xrandr --output HDMI1 --auto --output LVDS1 --auto --output VGA1 --auto
