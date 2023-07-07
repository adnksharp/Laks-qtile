from libqtile.config import Key, Group, Drag
from libqtile.lazy import lazy
from .scripts import *

meta = 'mod4'
alt = 'mod1'
ctrl = 'control'
shift = 'shift'

keys = [ Key(key[0], key [1], *key[2:]) for key in [
    ([meta], 'down', lazy.layout.down()),
    ([meta], 'up', lazy.layout.up()),
    ([meta], 'left', lazy.layout.left()),
    ([meta], 'right', lazy.layout.right()),
    ([alt], 'Tab', lazy.layout.next()),
    ([meta, ctrl], 'right', lazy.screen.next_group()),
    ([meta, ctrl], 'left', lazy.screen.prev_group()),

    ([meta, alt], 'down', lazy.layout.shuffle_down()),
    ([meta, alt], 'up', lazy.layout.shuffle_up()),
    ([meta, alt], 'left', lazy.layout.shuffle_left()),
    ([meta, alt], 'right', lazy.layout.shuffle_right()),
    ([meta], 'Tab', lazy.next_layout()),
    ([meta, alt], 'Tab', lazy.layout.toggle_split()),

    ([meta, shift], 'down', lazy.layout.grow_down()),
    ([meta, shift], 'up', lazy.layout.grow_up()),
    ([meta, shift], 'left', lazy.layout.grow_left()),
    ([meta, shift], 'right', lazy.layout.grow_right()),
    ([meta, shift], 'Tab', lazy.layout.normalize()),
    ([meta], 'Escape', lazy.window.toggle_floating()),

    ([meta, alt], 'F4', lazy.shutdown()),
    ([meta], 'q', lazy.window.kill()),
    ([], 'F4', lazy.spawn('xset dpms force off')),
    ([meta], 'space', lazy.widget["keyboardlayout"].next_keyboard()),

    ([meta], 'Return', lazy.spawn('alacritty')),
    ([meta], 'a', lazy.spawncmd()),

    ([meta], 'Insert', lazy.spawn('pactl set-sink-mute @DEFAULT_SINK@ toggle')),
    ([meta], 'Delete', lazy.spawn('playerctl play-pause')),
    ([meta], 'Home', lazy.spawn('playerctl previous')),
    ([meta], 'End', lazy.spawn('playerctl next')),
    ([meta], 'Prior', lazy.spawn('pactl set-sink-volume @DEFAULT_SINK@ +5%')),
    ([meta], 'Next', lazy.spawn('pactl set-sink-volume @DEFAULT_SINK@ -5%')),

    ([ctrl], 'Escape', lazy.spawn('rofi -show drun -theme gnome')),
    ([meta], 'grave', lazy.spawn('rofi -show window -theme config')),
    ([meta], 'm', lazy.spawn('zsh .config/rofi/scripts/browser.sh')),
    ([], 'XF86PowerOff', lazy.spawn('zsh .config/rofi/scripts/powermenu.sh')),
    ]
]

groups = [Group(i) for i in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']]
for i, group in enumerate(groups):
    if i < 9:
        keys.extend([
            Key([meta], str(i+1), lazy.group[group.name].toscreen(), lazy.spawn(wallpaper())),
            Key([meta, shift], str(i+1), lazy.window.togroup(group.name), lazy.spawn(wallpaper())),
        ])
    else:
        keys.extend([
            Key([meta, ctrl], str(i-8), lazy.group[group.name].toscreen(), lazy.spawn(wallpaper())),
            Key([meta, ctrl, shift], str(i-8), lazy.window.togroup(group.name), lazy.spawn(wallpaper())),
        ])

mouse = [
    Drag([meta], 'Button1', lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([meta], 'Button3', lazy.window.set_size_floating(), start=lazy.window.get_size()),
]
