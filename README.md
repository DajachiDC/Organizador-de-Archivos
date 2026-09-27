# 📁 Organizador de Archivos

Programa desarrollado en **Python** para organizar automáticamente los archivos de una carpeta según su extensión.

El programa detecta la extensión de cada archivo y lo mueve a una carpeta correspondiente. También permite listar las carpetas, subcarpetas y archivos existentes en una ruta.

---

## 🚀 Características

* 📂 Organización automática de archivos.
* 🔎 Detección de extensiones.
* 📁 Creación automática de carpetas.
* 🔄 Movimiento de archivos mediante `shutil`.
* 📋 Listado de carpetas, subcarpetas y archivos.
* 🖥️ Interfaz mediante consola.
* ⚡ No requiere librerías externas.
* 🪟 Compatible con Windows y otros sistemas que soporten Python.

---

## 🛠️ Tecnologías utilizadas

El proyecto utiliza módulos incluidos en Python:

```python
import os
import shutil
from time import sleep
```

### `os`

Se utiliza para:

* Comprobar si una ruta existe.
* Recorrer directorios.
* Obtener extensiones.
* Crear carpetas.
* Cambiar de directorio.
* Limpiar la consola.

### `shutil`

Se utiliza principalmente para mover archivos:

```python
shutil.move()
```

### `time.sleep`

Se utiliza para crear pequeñas pausas en el menú y mostrar mensajes.

---

## 📂 Estructura

```text
OrganizadorDeArchivos/
│
├── main.py
└── README.md
```

> El nombre del archivo Python puede ser diferente dependiendo de cómo hayas guardado el proyecto.

---

## ▶️ Ejecución

Primero necesitas tener instalado Python.

Puedes comprobarlo ejecutando:

```bash
python --version
```

Después ejecuta el programa:

```bash
python main.py
```

---

## 🖥️ Menú principal

Al ejecutar el programa encontrarás:

```text
+-----------------------------+
ORGANIZADOR DE ARCHIVOS
+-----------------------------+

OPCIONES:

1. Organizar
2. Listar
0. Salir
```

---

## 📁 Organizar archivos

La opción **1. Organizar** solicita la ruta donde se encuentran los archivos:

```text
Ingrese la ruta donde tienes los archivos:
```

Por ejemplo:

```text
C:\Users\David\Downloads
```

El programa analiza los archivos de esa carpeta y los organiza según su extensión.

### Ejemplo

Antes:

```text
Downloads/
├── programa.py
├── foto.jpg
├── musica.mp3
├── documento.pdf
└── proyecto.html
```

Después:

```text
Downloads/
├── Python/
│   └── programa.py
│
├── Imágenes/
│   └── foto.jpg
│
├── Música/
│   └── musica.mp3
│
├── PDF/
│   └── documento.pdf
│
└── HTML/
    └── proyecto.html
```

Las carpetas necesarias se crean automáticamente.

---

## 📋 Listar archivos

La opción:

```text
2. Listar
```

permite visualizar la estructura de una ruta.

Ejemplo:

```text
Carpeta: 'C:\Users\David\Downloads'
Subcarpetas: ['Python', 'Imágenes', 'PDF']
Archvios:
    - ejemplo.txt
    - programa.py
```

El programa utiliza:

```python
os.walk()
```

para recorrer las carpetas y subcarpetas.

---

## 🗂️ Extensiones compatibles

El programa contiene una lista amplia de extensiones.

### 🐍 Python

```text
.py
.pyw
.pyc
.pyo
```

### 🌐 Desarrollo web

```text
.html
.htm
.css
.js
.jsx
.ts
.tsx
.json
.xml
.php
.asp
.aspx
.jsp
```

### ☕ Java / C / C++ / C#

```text
.java
.class
.jar
.c
.h
.cpp
.cc
.cxx
.hpp
.cs
.csproj
.sln
```

### 🤖 Arduino

```text
.ino
.hex
.bin
.elf
```

### 📝 Documentos

```text
.txt
.md
.rtf
.doc
.docx
.odt
.pdf
.xls
.xlsx
.csv
.ppt
.pptx
.odp
```

### 🖼️ Imágenes

```text
.jpg
.jpeg
.png
.gif
.bmp
.webp
.svg
.ico
.tiff
.tif
.raw
.psd
.ai
```

### 🎵 Audio

```text
.mp3
.wav
.flac
.aac
.ogg
.m4a
.wma
.mid
.midi
```

### 🎬 Vídeo

```text
.mp4
.mkv
.avi
.mov
.wmv
.flv
.webm
.m4v
.mpeg
.mpg
```

### 📦 Archivos comprimidos

```text
.zip
.rar
.7z
.tar
.gz
.bz2
.xz
```

### 💿 Instaladores y ejecutables

```text
.exe
.msi
.msix
.appx
.apk
.deb
.rpm
```

### 🗄️ Bases de datos

```text
.db
.sqlite
.sqlite3
.sql
.mdb
.accdb
```

### 💻 Scripts

```text
.bat
.cmd
.ps1
.sh
.bash
.zsh
```

### 🎮 Minecraft

```text
.schem
.schematic
.mcfunction
.mcmeta
.nbt
```

También se incluyen extensiones para:

* ⚙️ Archivos del sistema
* 🔐 Certificados
* 🧩 Configuración
* 📚 Libros digitales
* 🖥️ Discos virtuales
* 🔤 Fuentes
* 📋 Copias de seguridad
* 🌐 Torrents

---

## 🔧 ¿Cómo funciona?

El programa utiliza un diccionario para relacionar extensiones con carpetas:

```python
nombre_carpetas = {
    ".py": "Python",
    ".html": "HTML",
    ".css": "CSS",
    ".js": "JavaScript",
    ".jpg": "Imágenes",
    ".mp3": "Música",
    ".mp4": "Vídeos"
}
```

Después obtiene la extensión:

```python
nombre, ext = os.path.splitext(archivo)
```

Y comprueba si está registrada:

```python
if ext in nombre_carpetas.keys():
```

Si existe, crea la carpeta:

```python
os.makedirs(nombre_carpetas[ext], exist_ok=True)
```

Finalmente mueve el archivo:

```python
shutil.move(ruta_archivo, nombre_carpetas[ext])
```

---

## ⚠️ Importante

Antes de utilizar la opción **Organizar**, se recomienda realizar una copia de seguridad de los archivos importantes.

El programa **mueve los archivos físicamente** a otras carpetas, por lo que la estructura original del directorio cambiará.

Los archivos cuya extensión no esté incluida en el diccionario actualmente no son movidos.

---

## 👨‍💻 Autor

**Dajachi**

Proyecto realizado como práctica de programación en **Python**, trabajando con manejo de archivos, directorios, diccionarios y automatización.

---

## 📜 Licencia

Este proyecto puede utilizarse, modificarse y adaptarse para fines educativos y personales.
