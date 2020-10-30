# Descarga automatizada de Platzi

Descarga automática de los cursos de Platzi con un script creado en Python utilizando `youtube-dl` como un subproceso. El script es un fork de [`leethobbit`](https://github.com/leethobbit/pluradl.py) para `Pluralsight`, yo solo he modificado su uso para `Platzi`. Abajo dejo ejemplos de cómo se debe utilizar y las herramientas necesarias. 

**Aprovechando el PlatziDay te puedes crear una cuenta gratuita con acceso a todos los cursos durante 48h. Nota: te restringen un total de 150 clases tomadas.**

## Tener Python instalado

[`Python`](https://www.python.org/) **y establecida su ruta en el PATH.**

## Instalacion youtube-dl

##### **macOS/UNIX**

Con [`brew`](https://brew.sh/) para macOS:

```bash
brew install youtube-dl
```

Con [`npm`](https://www.npmjs.com/):

```bash
npm install youtube-dl
```

Con [`pacman`](https://www.archlinux.org/packages/community/any/youtube-dl/)

```
pacman -S youtube-dl
```

O puedes `curl`/`wget` :

```bash
sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl
```
```bash
sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl
```


##### Windows

Descargar con npm como arriba mencionado o descargar el archivo `exe`del link de abajo [añade el `exe` en tu_PATH_](https://youtube-dl.org/).

O usar [`pip`](https://pypi.org/project/youtube_dl/) para actualizar una vez instalado
```bash
pip install youtube_dl
```

[Source: youtube-dl download](https://youtube-dl.org/)

## Instalacion de ffmepg

Descargar el archivo para tu plataforma desde (https://ffmpeg.org/). Esta herramienta permite la conversión del formato de los vídeos a **mp4.**
**En Windows descomprimir el .zip y añadir su ruta al path**

## Instrucciones

#### Descarga de **Platzi** con `platzi.dl`
Después de instalar youtube-dl (y que esté disponible como variable de entorno) asegúrate de tener [`courselist.txt`] en el directorio de [`platzidl.py`] en el añadirás el ID de cada clase **listadas línea por línea**. El ID de las clases lo tomas de la URL de Platzi ejemplo: [https://platzi.com/clases/1318-django/12398-introduccion-al-curso5511](https://platzi.com/clases/1318-django/12398-introduccion-al-curso5511) Donde el ID es "1318-django/12398-introduccion-al-curso5511". 

**Nota: Una vez abres una clase te la cuenta como vista, tomando en cuenta el límite de solo 150 clases permitidas, un consejo para no gastarte las clases es que copies el link directamente del código fuente [`Ctrl+Shift+I`] en **Chrome** 

Luego ejecuta el script `platzidl.py` para descargar todas las clases que tengas en [`courselist.txt`]. Los vídeos se descargarán automáticamente en la carpeta Courses y serán acomodados en el orden las clases como aparecen en [`courselist.txt`]. Solo tienes que reemplazar los creedenciales de ejemplo abajo mostrados con los tuyos propios de platzi y a descargar ...

```bash
python platzidl.py
      .
      .
      .
Ingresa tus credenciales de Platzi
Enter username: tuemail@ejemplo.com
Enter password (will no be displayed)
: yourPassword
```

... con `courselist.txt` en el mismo directorio de `platzidl.py` ...

courselist.txt
```notepad
1318-django/12398-introduccion-al-curso5511
1318-django/12399-historia-de-web-development
1318-django/12400-preparacion-del-entorno-de-trabajo-en-mac
1318-django/12402-creacion-del-proyecto-platzigram-tu-primer-hola-mu
1318-django/12403-el-objeto-request2427
1318-django/12404-solucion-al-reto-pasando-argumentos-en-la-url
1318-django/12405-creacion-de-la-primera-app
1318-django/12406-introduccion-al-template-system
1318-django/12407-patrones-de-diseno-y-django
1318-django/12408-la-quotmquot-en-el-mtv
1318-django/12409-el-orm-de-django
1318-django/12411-extendiendo-el-modelo-de-usuario
1318-django/12412-implementacion-del-modelo-de-usuarios-de-platzigra
1318-django/12413-explorando-el-dashboard-de-administracion
1318-django/12414-dashboard-de-administracion
1318-django/12415-creacion-del-modelo-de-posts
1318-django/12416-templates-y-archivos-estaticos
1318-django/12417-login
1318-django/12418-logout6923
1318-django/12419-signup
1318-django/12420-middlewares9277
1318-django/12421-formularios-en-django6487
1318-django/12396-mostrando-el-form-en-el-template
1318-django/12422-model-forms
1318-django/12423-validacion-de-formularios
1318-django/12424-class-based-views
1318-django/12425-protegiendo-la-vista-de-perfil-detail-view-y-list-
1318-django/12427-createview-formview-y-updateview
1318-django/12428-generic-auth-views
1318-django/12527-arquirectura-conceptos-componentes
1318-django/12571-como-conectar-django-a-una-base-de-datos
1318-django/12529-configurar-el-servidor
1318-django/12535-preparacion-del-vps-en-aws
1318-django/12429-conclusiones-del-curso
1318-django/12430-como-usar-los-templates-en-django
.
.
.
```

# IMPORTANTE
El parámetro `SLEEP_INTERVAL = 120` usado en el script [`platzidl.py`] es para que el programa espere al menos 120s (2 minutos) antes de descargar la siguiente clase. Si no lo usas puede haber riesgo de ser baneado por demasiadas peticiones. **Nota:** el riesgo de ban no lo he comprobado yo, sin embargo es un parámetro que incluye el script original por las restricciones de `Pluralsight`. Desconozco si `Platzi` pueda bloquear cuentas por la misma razón.
