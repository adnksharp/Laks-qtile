from libqtile import layout
from libqtile.command import lazy
from libqtile.config import Match

# Configuracion de ventanas normales
layoutCfg = {
    'border_width': 0,
    'margin': 4
}

# Configuracion de ventanas flotantes
flayoutCfg = {
    'float_rules': '[*layout.Floating.default_float_rules,]',
    'border_width': 0,
    'fullscreen_border_width': 0,
    'max_border_width': 0,
}

layouts = [
    # Reglas de ventanas
    layout.Columns ( **layoutCfg ),
    layout.Max ( ),
    layout.Zoomy ( **layoutCfg ),
    layout.Floating ( **flayoutCfg )
]

floating_layout = layout.Floating ( 
    float_rules = [ *layout.Floating.default_float_rules, ],
    border_width = 0,
    fullscreen_border_width = 0,
    max_border_width = 0,
 )
