import random, subprocess
from os import path, listdir

def wallpaper():
    pictures = listdir(path.expanduser("~/Imágenes/Wallpaper/"))
    wallpaper = []
    for picture in pictures:
        wallpaper.append(path.expanduser(f"~/Imágenes/Wallpaper/{picture}"))
    feh = random.choice(wallpaper)
    pic = listdir(feh)
    pic = random.choice(pic)
    feh = feh + '/' + pic
    feh = 'feh --bg-fill ' + feh
    return feh

def first():
    sh = 'alacritty & picom & onedrive --monitor --confdir ~/.config/onedrive & ' + wallpaper()
    subprocess.run(sh, shell=True)

def set_wallpaper():
    subprocess.run(wallpaper(), shell=True)
