from libqtile.config import Screen
from libqtile import bar
from libqtile.log_utils import logger
from settings.Theme.widgets import MainWidgets, extraWidgets
import subprocess

# Configuracion de barras de cada pantalla
def qBar ( widgets, opc ):
    return bar.Bar ( widgets, 24, opacity=opc )

# Leer la cantidad de pantallas conectadas
xrandr = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"
command = subprocess.run (
    xrandr,
    shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE,
)

if command.returncode != 0:
    monitors = 1
else:
    monitors = int ( command.stdout.decode ( "UTF-8" ) )

# Configuracion de pantallas
screens = [ Screen ( top = qBar ( MainWidgets, 1 ) ) ]
if monitors > 1:
    for _ in range ( 1, monitors ):
        screens.append ( Screen ( top = qBar ( extraWidgets, 1 ) ) )
