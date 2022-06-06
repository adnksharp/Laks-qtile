from libqtile.config import Drag, Click
from libqtile.command import lazy
from .keyboard import meta


mouse = [
    Drag (
        # Cambiar la posicion de la ventana flotante
        [ meta ], "Button1",
        lazy.window.set_position_floating ( ), start = lazy.window.get_position ( )
    ),
    Drag(
        # Cambiar el tamaño de la ventana flotante
        [ meta ], "Button3",
        lazy.window.set_size_floating ( ), start=lazy.window.get_size ( )
    ),
]
