from libqtile import widget 
from .theme import *

# Colores de los widgets
def colors ( wFg = ForegroundColor, wBg = BackgroundColor ):
    return {
        'foreground': wFg,
        'background': wBg
    }

# Fuente de los widgets
def fonts ( fFamily = 'Hack Nerd Font mono', fSize = 14 ):
    return {
        'font': fFamily, 
        'fontsize': fSize
    }

# Separador de widgets
def separator ( pad = 10 ):
    return widget.Sep ( **colors ( ), linewidth = 0, padding = pad )

# Widget de iconos 
def icons ( fg = ActiveColor, bg = BackgroundColor, fontsize = 19, text = "?" ):
    return widget.TextBox (
        **colors ( wFg = fg, wBg = bg ),
        **fonts ( fSize = fontsize ),
        text = text,
        padding = 3
    )

# Widget de escritorios 
def workspaces ( ):
    return widget.GroupBox ( 
        **colors ( wFg = ForegroundColori ),
        **fonts ( fSize = 19 ), 
        padding = 2, 
        border_width = 0,
        rounded = False,
        disable_drag = True,
        highlight_method = 'text',
        urgent_alert_method = 'text',
        active = ActiveColor, 
        inactive = InactiveColor, 
        urgent_border = UrgentColor,
        this_screen_border = BasicColor,
        other_screen_border = BasicColor,
        this_current_screen_border = BasicColor,
        other_current_screen_border = BasicColor,
    )

# Widget de distribuciones de teclado
def inputs ( ):
    return widget.KeyboardLayout ( 
        **fonts ( ),
        configured_keyboards = [ 
            'dvorak', 
            'latam dvorak', 
            'us' ], 
        display_map = { 
            'dvorak':'dv', 
            'latam dvorak': 'lat', 
            'us':'us' }, 
    )

# Widgets de la pantalla principal
MainWidgets = [
    workspaces ( ),
    widget.WindowName ( **colors ( wFg = BasicColor ), **fonts ( fFamily = 'SF Compact Rounded' ) ),
    icons ( fg = PinkColor, text = ':' ),
    widget.PulseVolume ( **fonts ( ) ),
    separator ( ),
    icons ( fg = BlueColor,  text = ':' ),
    widget.CPU ( **colors ( wFg = ForegroundColori ), **fonts ( ),
        format = '{load_percent}%' 
    ),
    separator ( ),
    icons ( fg = TealColor, text = ':' ),
    widget.CurrentLayout ( **colors ( wFg = BasicColor ), **fonts ( ) ),
    separator ( ),
    icons ( fg = AmberColor, text = ':' ),
    widget.Clock ( **colors ( wFg = ForegroundColori ), **fonts ( ), 
        format = '%H:%M:%S' 
    ),
    separator ( ),
]

# Widgets de la pantalla secundaria
extraWidgets = [
    widget.WindowName ( **colors ( wFg = BasicColor ), **fonts ( fFamily = 'SF Compact Rounded') ),
    widget.Systray ( background = BackgroundColor ),
    separator ( ),
    icons ( fg = PinkColor, text = ':' ),
    inputs ( ),
    separator ( ),
    icons ( fg = BlueColor, text = ':' ),
    widget.Memory ( **colors ( wFg = ForegroundColori ), **fonts ( ), 
        format = '{MemPercent: .0f}%' 
    ),
    separator ( ),
    icons ( fg = TealColor, text = ':' ),
    widget.CurrentLayout ( **colors ( wFg = BasicColor ), **fonts ( ) ),
    separator ( ),
    icons ( fg = AmberColor, text = ':' ),
    widget.Clock ( **colors ( wFg = ForegroundColori ), **fonts ( ), 
        format = '%d/%m/%Y' 
    ),
    separator ( ),
]

# Configuracion de los widgets por defecto
widgetDefaults = {
    'font': 'Hack Nerd Font mono',
    'fontsize': 14,
    'padding': 1,
}
extensionDefaults = widgetDefaults.copy ( )