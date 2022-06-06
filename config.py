from libqtile import hook
from libqtile import qtile
from settings.Peripheral.keyboard import meta, keys
from settings.Peripheral.desktop import groups
from settings.Process.layouts import layouts, floating_layout
from settings.Theme.widgets import widgetDefaults, extensionDefaults
from settings.Process.screens import screens
from settings.Peripheral.mouse import mouse
from settings.Process.path import qtile_path
from os import path
import subprocess

# Ejecutar autostart.sh
@hook.subscribe.startup_once
def autostart ( ):
    subprocess.call ( [ path.join ( qtile_path, 'autostart.sh' ) ] )

main = None
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
auto_minimize = True
focus_on_window_activation = 'smart'
wmname = 'LG3D'
