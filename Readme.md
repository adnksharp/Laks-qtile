# Mi configuracion de Qtile

![K-045.jpg](https://i.postimg.cc/K8qXCpR8/K-045.jpg)

Mis archivos de configuración de qtile para un diseño de teclado dvorak y preferiblemente para dos monitores.

## Paquetes recomendados

- [Picom](https://wiki.archlinux.org/title/Picom)

# Archivos

    .config
    └──qtile
        ├── autostart.sh
        ├── config.py
        └── settings
            ├── __init__.py
            ├── Peripheral
            │   ├── desktop.py
            │   ├── keyboard.py
            │   ├── mouse.py
            ├── Process
            │   ├── layouts.py
            │   ├── path.py
            │   └── screens.py
            └── Theme
                ├── theme.py
                └── widgets.py

### [config](config.py)
Es el archivo que ejecuta qtile, el cual se dividió en módulos alojados en la carpeta [settings](settings/), los cuales se importan con la instrucción **import**.

### [autostart](autostart.sh)
Ejecuta instrucciones en bash para:
- Definir la distribucion de teclado en **dvorak**
- Iniciar picom y la terminal 
- Definir un fondo de pantalla con [feh](https://wiki.archlinux.org/title/Feh#Set_the_wallpaper)
- Deshabilitar el apagado automático de la pantalla
- Configurar la resolución de las pantallas conectadas con [xrandr](https://wiki.archlinux.org/title/Xrandr)
# Peripheral
Contiene configuraciones para el mouse, teclado y escritorios virtuales (grupos).

### [keyboard](settings/Peripheral/keyboard.py)
La configuracion de teclas esta diseñada para una distribucion de teclado dvorak y clasificado segun las teclas especiales usadas:

#### Meta 

|        | Atajo         | Acción |
|--------|---------------|--------|
| [1-8]  | [1-8]         | Cambia el foco al grupo indicado |
| O      | O             | Cambia a la ventana inferior                    |
| ,      | Comma         | Cambia a la ventana superior                    |
| A      | A             | Cambia a la ventana derecha                     |
| E      | E             | Cambia a la ventana izquierda                   |
| Esc    | Escape        | Hace/Deshace una ventana flotante               |
| Q      | Q             | Cierra una ventana                              |
| '      | Apostrofe     | Cambia al grupo del monitor anterior            |
| .      | Punto         | Cambia al grupo del siguiente monitor           |
| Tab    | Tabulador     | Cambia la forma en que se muestran las ventanas |
| ;      | Punto y coma  | Lanza el menú de aplicaciones                   |
|        | Espacio       | Cambia la distribucion de teclado               |
| Enter  | Enter         | Lanza la terminal de Alacritty                  |
| W, V, Z| W, V, Z       | Abre aplicaciones                               |
| T, N, S| T, N, S       | Abre aplicaciones                               | 
| C, R, L| C, R, L       | Abre aplicaciones                               |

#### Meta + Alt

|        | Atajo         | Acción |
|--------|---------------|--------|
| O      | O             | Mueve la ventana a la parte inferior            |
| ,      | Comma         | Mueve la ventana a la parte superior            |
| A      | A             | Mueve la ventana a la parte derecha             |
| E      | E             | Mueve la ventana a la parte izquierda           |
| Tab    | Tabulador     | Cambia la forma en que se muestran las ventanas |
| W      | W             | Di-sminuye el volumen de salida                 |
| V      | V             | Silencia/Activa la salida de audio              | 
| Z      | Z             | Aumenta el volumen de salida                    |
| T      | T             | Regresa al elemento de reproduccion antearior   |
| N      | N             | Pausa/Reproduce el elemento de reproduccion     | 
| S      | S             | Cambia al elemento de reproduccion siguiente    |
| C      | C             | Toma una captura de pantalla                    |
| R      | R             | Toma una captura de pantalla despues de 5s      | 
| L      | L             | Toma una captura de una region seleccionada     |

#### Meta + Control

|        | Atajo         | Acción |
|--------|---------------|--------|
| [1-8]  | [1-8]         | Cambia al grupo indicado y el fondo de pantalla |
| O      | O             | Cambia el tamaño de la ventana                  |
| ,      | Comma         | Cambia el tamaño de la ventana                  |
| A      | A             | Cambia el tamaño de la ventana                  |
| E      | E             | Cambia el tamaño de la ventana                  |
| Esc    | Escape        | Reinicia Qtile                                  |
| W, V, Z| W, V, Z       | Abre URLs desde el navegador                    |
| T, N, S| T, N, S       | Abre URLs desde el navegador                    | 
| C, R, L| C, R, L       | Abre URLs desde el navegador                    |

#### Meta + Shift
|        | Atajo         | Acción |
|--------|---------------|--------|
| [1-8]  | [1-8]         | Cambia la ventana al grupo indicado |

#### Control + Escape
Muestra las ventanas abiertas

#### F3 
Deactiva el apagado de pantalla por inactividad

#### F4
Apaga las pantallas

### [desktop](settings/Peripheral/desktop.py)
definen los grupos enumerados con iconos de **Nerd Fonts** y los atajos para cambiar entre ellos.

### [mouse](settings/Peripheral/mouse.py)
Define las teclas del mouse para mover ventas flotantes y redimensionarlas

## Process
Lee los monitores conectados, define las barras para cada pantalla y el acceso a la rapeta de configuarcion de qtile (~/.config/qtile)

### [layouts](settings/Process/layouts.py)
Define la forma en que se pueden mostrar las ventanas y el tamaño de los bordes

### [screens](settings/Process/screens.py)
Lee la cantidad de ventanas conectadas y la barra para cada una de estas

### [path](settings/Process/path.py)
Permite al archivo config trabajar con el archivo autostart tomando como base la carpeta [~/.config/qtile]()

## Theme
Contiene la configuración de los widgets de cada barra y los colores usados

### [theme](settings/Theme/theme.py)

<p style="color: #000" > 
Color de fuentes 1: Foreground | #000
</p>

<p style="color: #aaa" >
Color de fuentes 2: Foregroundi | #aaa
</p>

<p style="color: #808888" >
Color de fondo: Background | #808888
</p>

<p style="color: #fff" >
Color neutro 1: BasicColor | #fff
</p>

<p style="color: #97b1b6" >
Color neutro 2: ActiveColor | #97b1b6
</p>

<p style="color: #3f575b" >
Color neutro 3: InactiveColor | #3f575b
</p>

<p style="color: #e55a44" >
Color de alerta: UrgentColor | #e55a44
</p>

<p style="color: #ef4abe" >
Resaltado 1: RedColor | #ef4abe
</p>
<p style="color: #ec4aef" >
Resaltado 2: PinkColor | #ec4aef
</p>

<p style="color: #4cc1c9" >
Resaltado 3: BlueColor | #4cc1c9
</p>

<p style="color: #3e9ea5" >
Resaltado 4: PurpleColor | #3e9ea5
</p>

<p style="color: #62fcc9" >
Resaltado 4: TealColor | #62fcc9
</p>

<p style="color: #fcc920" >
Resaltado 5: AmberColor | #fcc920
</p>

### [widgets](settings/Theme/widgets.py)
Los elementos que se muestran en la barra de cada pantalla estan agrupados segun la pantalla en que son utilizados

#### Pantalla principal

- Grupos
- Nombre de la ventana
- Control de volumen
- Monitor de uso de CPU
- Forma en la que se muestan las ventanas: [Columnas, Max, Zoomy o floatantes](http://docs.qtile.org/en/latest/manual/ref/layouts.html)
- Hora

#### Pantalla secundaria

- Nombre de la ventana
- Iconos del sistema
- Distribucion de teclado usada
- Monitor de uso de memoria RAM
- Forma en la que se muestan las ventanas: [Columnas, Max, Zoomy o floatantes](http://docs.qtile.org/en/latest/manual/ref/layouts.html)
- Fecha
