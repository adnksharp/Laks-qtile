from libqtile.config import Screen
from libqtile import bar, widget

def icon(name):
    return widget.TextBox(
        text=name,
        font='Symbols Nerd Font Mono',
        fontsize=14,
        padding=0,
    )

widget_defaults = dict(
    font='SF Pro Rounded',
    fontsize=14,
    padding=2,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(4),
                widget.TextBox(text='>_'),
                widget.WindowName(
                    format='{name}',
                    max_chars=90,
                ),
                widget.Spacer(),
                widget.Clock(format='%H:%M'),
                widget.Spacer(4),
                widget.Prompt(prompt='$ '),
                widget.Spacer(),
                widget.Systray(),
                widget.Spacer(4),
                icon('󱄠'),
                widget.PulseVolume(
                    volume_app='pavucontrol',
                    mouse_callbacks={
                        'Button1': lambda: None,
                        'Button2': lambda: None,
                        'Button3': lambda: None,
                    },
                    scroll=False,
                    step=5,
                ),
                widget.Spacer(4),
                widget.Battery(
                    full_char='󱊣',
                    charge_char='󱊥',
                    discharge_char='󱊢',
                    format='{char} {percent:2.0%}',
                    hide_threshold=0.99,
                ),
                widget.Spacer(4),
                widget.KeyboardLayout(
                    configured_keyboards=['us dvorak', 'latam dvorak', 'us' ],
                    display_map={
                        'us dvorak': '', 'latam dvorak': '󰅣', 'us': '󰸊'},
                    mouse_callbacks={
                        'Button1': lambda: None,
                        'Button2': lambda: None,
                        'Button3': lambda: None,
                    },
                    font='Symbols Nerd Font Mono',
                    fontsize=14,
                    padding=0,
                ),
                widget.Spacer(4),
                widget.CurrentLayout(
                    max_chars=1,
                    padding=0
                ),
            ],
            24,
            opacity=0.6,
        ),
    ),
]
