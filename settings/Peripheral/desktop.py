from libqtile.config import Key, Group
from libqtile.command import lazy
from .keyboard import meta, shift, keys

# Esritorios virtuales
groups = [ Group ( i ) for i in [ '', '', '', 'ﭮ', '', '﬏', '', '' ] ]

for i, group in enumerate ( groups ):
    actual_key = str ( i + 1 )
    keys.extend ( [
        # Mover el foco a actual_key escritorio
        Key ( [ meta ], actual_key, lazy.group [ group.name ].toscreen ( ) ),
        
        # Mover ventana a actual_key escritorio
        Key ( [ meta, shift ], actual_key, lazy.window.togroup ( group.name ) )
    ] )
