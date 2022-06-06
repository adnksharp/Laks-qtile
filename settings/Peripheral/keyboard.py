from libqtile.config import Key
from libqtile.command import lazy

# Renombrar teclas especiales
meta = 'mod4'
alt = 'mod1'
shift = 'shift'
control = 'control'

keys = [ Key ( key [ 0 ], key [ 1 ], *key [ 2: ] ) for key in [
    # Cambiar el foco entre ventanas
    ( [ meta ], 'o', lazy.layout.down ( ) ),
    ( [ meta ], 'comma', lazy.layout.up ( ) ),
    ( [ meta ], 'a', lazy.layout.left ( ) ),
    ( [ meta ], 'e', lazy.layout.right ( ) ),

    # Mover ventanas de posicion
    ( [ meta, alt ], 'o', lazy.layout.shuffle_down ( ) ),
    ( [ meta, alt ], 'comma', lazy.layout.shuffle_up ( ) ),
    ( [ meta, alt ], 'a', lazy.layout.shuffle_left ( ) ),
    ( [ meta, alt ], 'e', lazy.layout.shuffle_right ( ) ),

    # Cambiar el tamaño de la ventana
    ( [ meta, control ], 'o', lazy.layout.grow_down ( ) ),
    ( [ meta, control ], 'comma', lazy.layout.grow_up ( ) ),
    ( [ meta, control ], 'a', lazy.layout.grow_left ( ) ),
    ( [ meta, control ], 'e', lazy.layout.grow_right ( ) ),

    # Intercambiar ventanas tipo flotante
    ( [ meta ], 'Escape', lazy.window.toggle_floating ( ) ),

    # Cerrar ventana
    ( [ meta ], 'q', lazy.window.kill ( ) ),

    # Cambiar de monitor
    ( [ meta ], 'apostrophe', lazy.prev_screen ( ) ),
    ( [ meta ], 'period', lazy.next_screen ( ) ),

    # Cambiar foco entre ventanas
    ( [ meta ], 'Tab', lazy.next_layout ( ) ),
    ( [ meta, alt ], 'Tab', lazy.prev_layout ( ) ),

    # Reiniciar Qtile
    ( [ meta, control], 'Escape', lazy.restart ( ) ),

    # Lanzar el menu de aplicaciones
    ( [ meta ], 'semicolon', lazy.spawn ( 'rofi -show drun -theme gnome' ) ),
    ( [ control ], 'Escape', lazy.spawn ( 'rofi -show window -theme base' ) ),

    # Cambiar distribucion de teclado
    ( [ meta ], 'space', lazy.spawn ( 'python Documentos/Betas/python/keyboard.py' ) ),

    # Apagar pantalla
    ( [ ], 'F4', lazy.spawn ( 'xset dpms force off' ) ),

    # Deactivar apagado de pantalla por inactividad
    ( [ ], 'F3', lazy.spawn ( 'xset s off s noblank -dpms' ) ),

    # Abrir terminal
    ( [ meta ], 'Return', lazy.spawn ( 'alacritty' ) ),

    # Lanzar aplicaciones
    ( [ meta ], 'w', lazy.spawn ( 'vivaldi-stable' ) ),
    ( [ meta ], 'v', lazy.spawn ( 'pavucontrol' ) ),
    ( [ meta ], 'z', lazy.spawn ( 'brave' ) ),
    ( [ meta ], 't', lazy.spawn ( 'pcmanfm' ) ),
    ( [ meta ], 'n', lazy.spawn ( 'teams-for-linux' ) ),
    ( [ meta ], 's', lazy.spawn ( 'code' ) ),
    ( [ meta ], 'c', lazy.spawn ( 'seahorse' ) ),
    ( [ meta ], 'r', lazy.spawn ( 'libreoffice' ) ),
    ( [ meta ], 'l', lazy.spawn ( 'notable' ) ),

    # Controlar el volumen
    ( [ meta, alt ], 'w', lazy.spawn ( 'pactl set-sink-volume @DEFAULT_SINK@ -5%' ) ),
    ( [ meta, alt ], 'v', lazy.spawn ( 'pactl set-sink-mute @DEFAULT_SINK@ toggle' ) ),
    ( [ meta, alt ], 'z', lazy.spawn ( 'pactl set-sink-volume @DEFAULT_SINK@ +5%' ) ),

    # Controlar la reproduccion multimedia
    ( [ meta, alt ], 't', lazy.spawn ( 'playerctl previous' ) ),
    ( [ meta, alt ], 'n', lazy.spawn ( 'playerctl play-pause' ) ),
    ( [ meta, alt ], 's', lazy.spawn ( 'playerctl next' ) ),

    # Capturar pantalla
    ( [ meta, alt ], 'c', lazy.spawn ( 'scrot Capturas/K.jpg' ) ),
    ( [ meta, alt ], 'r', lazy.spawn ( 'delay 5; scrot Capturas/K.jpg' ) ),
    ( [ meta, alt ], 'l', lazy.spawn ( 'scrot -s Capturas/K.jpg' ) ),

    # Abrir urls
    ( [ meta, control ], 'w', lazy.spawn ( '/usr/bin/brave --app=https://www.twitch.tv' ) ),
    ( [ meta, control ], 'v', lazy.spawn ( '/usr/bin/brave --app=https://open.spotify.com' ) ),
    ( [ meta, control ], 'z', lazy.spawn ( '/usr/bin/brave --app=https://www.youtube.com' ) ),
    ( [ meta, control ], 't', lazy.spawn ( '/usr/bin/brave --app=https://twitter.com/' ) ),
    ( [ meta, control ], 'n', lazy.spawn ( '/usr/bin/brave --app=https://www.facebook.com/' ) ),
    ( [ meta, control ], 's', lazy.spawn ( '/usr/bin/brave --app=https://www.instagram.com/' ) ),
    ( [ meta, control ], 'c', lazy.spawn ( '/usr/bin/brave --app=https://web.whatsapp.com/' ) ),
    ( [ meta, control ], 'r', lazy.spawn ( '/usr/bin/brave --app=https://www.reddit.com/' ) ),
    ( [ meta, control ], 'l', lazy.spawn ( '/usr/bin/brave --app=https://translate.google.com/' ) ),
]]
