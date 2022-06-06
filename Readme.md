# Dotfiles
Este repositorio contiene los archivos de configuración de qtile para un diseño de teclado dvorak y preferiblemente para dos monitores.

[![qtile.png](https://i.postimg.cc/kg6JgSBS/qtile.png)](https://postimg.cc/G4RwMHP3)

# Índice
- [Requisitos](#Requisitos) 
- [Archivos](#Archivos) 
  - [config](#config) 
  - [autostart](#autostart) 
  - settings
      - [Peripheral](#Peripheral)
        - [keyboard](#keyboard)  
        - [desktop](#desktop) 
        - [mouse](#mouse) 
     - [Process](#Process) 
        - [layouts](#layouts) 
        - [screens](#screens) 
        - [path](#path) 
      - [Theme](#Theme) 
        - [theme](#theme) 
        - [widgets](#widgets) 
- [Aplicaciones que uso](#Aplicaciones-que-uso)


# Requisitos

- [Qtile](https://wiki.archlinux.org/title/Qtile)

      pacman -S qtile

- [Picom](https://wiki.archlinux.org/title/Picom)

      pacman -S picom

- [Rofi](https://wiki.archlinux.org/title/Rofi)

      pacman -S picom

- [Nerd Fonts](https://www.nerdfonts.com)

      yay -S nerd-fonts-hack

- [Git](https://wiki.archlinux.org/title/Git_(Espa%C3%B1ol))

      pacman -S git



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
| O      | O             | Cambia el tamaño de la ventana                  |
| ,      | Comma         | Cambia el tamaño de la ventana                  |
| A      | A             | Cambia el tamaño de la ventana                  |
| E      | E             | Cambia el tamaño de la ventana                  |
| Esc    | Escape        | Reinicia Qtile                                  |
| W, V, Z| W, V, Z       | Abre URLs desde el navegador                    |
| T, N, S| T, N, S       | Abre URLs desde el navegador                    | 
| C, R, L| C, R, L       | Abre URLs desde el navegador                    |

#### Control + Escape
Muestra las ventanas abiertas

#### F3 
Deactiva el apagado de pantalla por inactividad

#### F4
Apaga las pantallaS

### [desktop](settings/Peripheral/desktop.py)
definen los grupos enumerados con iconos de **Nerd Fonts** y las teclas:
- **meta + [1-8]** para navegar entre grupos.
- **meta + shift + [1-8]** para mover ventanas a otros grupos.

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
Color de fuentes 1: Foreground
</p>

<p style="color: #aaa" >
Color de fuentes 2: Foregroundi
</p>

<p style="color: #808888" >
Color de fondo: Background
</p>

<p style="color: #fff" >
Color neutro 1: BasicColor
</p>

<p style="color: #97b1b6" >
Color neutro 2: ActiveColor
</p>

<p style="color: #3f575b" >
Color neutro 3: InactiveColor
</p>

<p style="color: #e55a44" >
Color de alerta: UrgentColor
</p>

<p style="color: #ef4abe" >
Resaltado 1: RedColor
</p>
<p style="color: #d64aef" >
Resaltado 2: PinkColor
</p>

<p style="color: #4ab5ef" >
Resaltado 3: BlueColor
</p>

<p style="color: #63fdd6" >
Resaltado 4: TealColor
</p>

<p style="color: #f7c931" >
Resaltado 5: AmberColor
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

# Aplicaciones que uso

## Terminal 

- [alacritty](https://wiki.archlinux.org/title/Alacritty#Configuration)
    
      pacman -S alacritty

- [tilix](https://github.com/gnunn1/tilix)

      pacman -S tilix

## Editores de texto

- [nvim](https://wiki.archlinux.org/title/Neovim)
      
      pacman -S neovim

- [visual-studio-code]()

      yay -S visual-studio-code-bin

## Gestores de archivos

- [pcmanfm]()

      pacman -S pcmanfm
- [ranger]()

      pacman -S ranger

## Navegadores

- [vivaldi](https://wiki.archlinux.org/title/Vivaldi)
      
      pacman -S vivaldi

- [brave](https://aur.archlinux.org/packages/brave-bin)

      yay -S brave-bin

## Controlador de volumen

- [pavucontrol](https://wiki.archlinux.org/title/PulseAudio)

      pacman -S pavucontrol

## Gestor de contraseñas

- [seahorse](https://wiki.archlinux.org/title/GNOME_(Espa%C3%B1ol)/Keyring_(Espa%C3%B1ol)#Claves_SSH)
      
      pacman -S seahorse gnome-keiring

## Oficina 

- [libreoffice](https://wiki.archlinux.org/title/LibreOffice_(Espa%C3%B1ol))
            
      pacman -S libreoffice-fresh libreoffice-fresh-es languajetool hunspell hunspell-es 

- [teams-for-linux](https://aur.archlinux.org/packages/teams-for-linux)

      yay -S teams-for-linux

- [notable](https://aur.archlinux.org/packages/notable-bin)

      yay -S notable

- [zathura](https://wiki.archlinux.org/title/Zathura)

      yay -S zathura zathura-pdf-poppler zathura-cb zathura-ps

## Extras

- [neofetch](https://wiki.archlinux.org/title/List_of_applications_(Espa%C3%B1ol)/Utilities_(Espa%C3%B1ol))

      pacman -S neofetch

- [cava](https://aur.archlinux.org/packages/cava)
      
      yay -S cava

- [gotop](https://aur.archlinux.org/packages/gotop)

      yay -S gotop

- [zsh](https://wiki.archlinux.org/title/Zsh_(Espa%C3%B1ol))

      pacman -S zsh
      sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

- [yay](https://aur.archlinux.org/packages/yay)

      git clone https://aur.archlinux.org/yay-bin.git
      cd yay-bin
      makepkg -si
