from libqtile import layout
from libqtile.config import Match

normal = {
    'border_width': 0,
    'margin': 6,
}
floatL = {
    'border_width': 0,
    'fullscreen_border_width': 0,
    'max_border_width': 0,
}

layouts = [
    layout.Columns(**normal),
    layout.Max(),
    layout.Floating(**floatL)
]

floating_layout = layout.Floating(
    **floatL,
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(wm_class='confirm'),
        Match(wm_class='dialog'),
        Match(wm_class='download'),
        Match(wm_class='error'),
        Match(wm_class='file_progress'),
        Match(wm_class='notification'),
        Match(wm_class='splash'),
        Match(wm_class='toolbar'),
        Match(title='Control de volumen'),
        Match(title='Personalizar apariencia y comportamiento'),
        Match(title='Brave'),
        Match(title='Picture-in-Picture'),
        Match(title='Pantalla en Pantalla'),
        Match(title='Android Emulator - AKDroid-33:5554'),
    ],
)
