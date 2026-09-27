import os
import shutil
from time import sleep


# -------------------------------------------------------------
#            FUNCIÓN PARA ORGANIZAR LOS ARCHIVOS
# -------------------------------------------------------------

def organizar_archivos(ruta):
    
    # Extensiones con su nombre de carpeta correspondiente
    nombre_carpetas = {
        # 🐍 Python
        ".py": "Python",
        ".pyw": "Python",
        ".pyc": "Python",
        ".pyo": "Python",

        # 🌐 Desarrollo web
        ".html": "HTML",
        ".htm": "HTML",
        ".css": "CSS",
        ".js": "JavaScript",
        ".jsx": "JavaScript",
        ".ts": "TypeScript",
        ".tsx": "TypeScript",
        ".json": "JSON",
        ".xml": "XML",
        ".php": "PHP",
        ".asp": "Web",
        ".aspx": "Web",
        ".jsp": "Web",

        # ☕ Java / C / C++ / C#
        ".java": "Java",
        ".class": "Java",
        ".jar": "Java",
        ".c": "C",
        ".h": "C",
        ".cpp": "C++",
        ".cc": "C++",
        ".cxx": "C++",
        ".hpp": "C++",
        ".cs": "C#",
        ".csproj": "C#",
        ".sln": "Visual Studio",

        # 🤖 Arduino / Electrónica
        ".ino": "Arduino",
        ".hex": "Arduino",
        ".bin": "Binarios",
        ".elf": "Arduino",

        # 📝 Documentos
        ".txt": "Texto",
        ".md": "Markdown",
        ".rtf": "Documentos",
        ".doc": "Word",
        ".docx": "Word",
        ".odt": "Documentos",
        ".pdf": "PDF",
        ".xls": "Excel",
        ".xlsx": "Excel",
        ".csv": "CSV",
        ".ppt": "PowerPoint",
        ".pptx": "PowerPoint",
        ".odp": "Presentaciones",

        # 🖼️ Imágenes
        ".jpg": "Imágenes",
        ".jpeg": "Imágenes",
        ".png": "Imágenes",
        ".gif": "Imágenes",
        ".bmp": "Imágenes",
        ".webp": "Imágenes",
        ".svg": "Imágenes",
        ".ico": "Iconos",
        ".tiff": "Imágenes",
        ".tif": "Imágenes",
        ".raw": "Imágenes",
        ".psd": "Photoshop",
        ".ai": "Illustrator",

        # 🎵 Audio
        ".mp3": "Música",
        ".wav": "Música",
        ".flac": "Música",
        ".aac": "Música",
        ".ogg": "Música",
        ".m4a": "Música",
        ".wma": "Música",
        ".mid": "MIDI",
        ".midi": "MIDI",

        # 🎬 Vídeo
        ".mp4": "Vídeos",
        ".mkv": "Vídeos",
        ".avi": "Vídeos",
        ".mov": "Vídeos",
        ".wmv": "Vídeos",
        ".flv": "Vídeos",
        ".webm": "Vídeos",
        ".m4v": "Vídeos",
        ".mpeg": "Vídeos",
        ".mpg": "Vídeos",

        # 📦 Comprimidos
        ".zip": "Comprimidos",
        ".rar": "Comprimidos",
        ".7z": "Comprimidos",
        ".tar": "Comprimidos",
        ".gz": "Comprimidos",
        ".bz2": "Comprimidos",
        ".xz": "Comprimidos",

        # 💿 Instaladores / Ejecutables
        ".exe": "Programas",
        ".msi": "Instaladores",
        ".msix": "Instaladores",
        ".appx": "Instaladores",
        ".apk": "Android",
        ".deb": "Linux",
        ".rpm": "Linux",

        # ⚙️ Windows / Sistema
        ".dll": "Sistema",
        ".sys": "Sistema",
        ".drv": "Drivers",
        ".ini": "Configuración",
        ".cfg": "Configuración",
        ".config": "Configuración",
        ".log": "Logs",
        ".tmp": "Temporales",

        # 🗄️ Bases de datos
        ".db": "Bases de datos",
        ".sqlite": "Bases de datos",
        ".sqlite3": "Bases de datos",
        ".sql": "SQL",
        ".mdb": "Access",
        ".accdb": "Access",

        # 💻 Scripts
        ".bat": "Scripts",
        ".cmd": "Scripts",
        ".ps1": "PowerShell",
        ".sh": "Shell",
        ".bash": "Shell",
        ".zsh": "Shell",

        # 🔐 Certificados / Seguridad
        ".pem": "Certificados",
        ".crt": "Certificados",
        ".cer": "Certificados",
        ".key": "Claves",
        ".p12": "Certificados",
        ".pfx": "Certificados",

        # 🧩 Configuración / Desarrollo
        ".env": "Configuración",
        ".gitignore": "Git",
        ".dockerfile": "Docker",
        ".yml": "Configuración",
        ".yaml": "Configuración",
        ".toml": "Configuración",
        ".lock": "Dependencias",

        # 🎮 Minecraft / Mods
        ".schem": "Minecraft",
        ".schematic": "Minecraft",
        ".mcfunction": "Minecraft",
        ".mcmeta": "Minecraft",
        ".nbt": "Minecraft",

        # 📚 Libros
        ".epub": "Libros",
        ".mobi": "Libros",
        ".azw": "Libros",
        ".azw3": "Libros",

        # 🖥️ Máquinas virtuales / Discos
        ".iso": "Imágenes de disco",
        ".vhd": "Discos virtuales",
        ".vhdx": "Discos virtuales",
        ".vmdk": "Discos virtuales",

        # 🔤 Fuentes
        ".ttf": "Fuentes",
        ".otf": "Fuentes",
        ".woff": "Fuentes",
        ".woff2": "Fuentes",

        # 📋 Otros
        ".bak": "Copias de seguridad",
        ".old": "Copias de seguridad",
        ".backup": "Copias de seguridad",
        ".torrent": "Torrents"
    }
        
    # Ir a la ruta digitada por el usuario
    os.chdir(ruta)
    
    print()
    
    # Recorrer todos los archivos de la ruta
    for archivo in os.listdir(ruta):
        
        # Verificar si el archivo es en realidad un archivo
        if os.path.isfile(archivo):
            
            # Obtener la ruta absoluta del archivo
            ruta_archivo = os.path.abspath(archivo)
            
            # Mostrar la ruta de cada archivo
            print(ruta_archivo)
        
            # Obtener el nombre del archivo y la extensión
            nombre, ext = os.path.splitext(archivo)
            
            # Verificar si la extensión del archivo está en el diccionario
            if ext in nombre_carpetas.keys():
                
                # Crear la carpeta según el archivo
                if ext in nombre_carpetas.keys():
                    os.makedirs(nombre_carpetas[ext], exist_ok=True)
                    
                shutil.move(ruta_archivo, nombre_carpetas[ext])
        
    print("\n[INFO] Los archivos se organizaron correctamente.")
    
    input("\nPresiona enter para continuar...\n")


# ------------------------------------------------------------------
#        FUNCIÓN PARA LISTAR ARCHIVOS, CARPETAS Y SUBCARPETAS
# ------------------------------------------------------------------

def listador(ruta):
    
    for carpeta, subcarpetas, archivos in os.walk(ruta):
        print(f"\nCarpeta: '{carpeta}'")
        print(f"Subcarpetas: {subcarpetas}")
        print("Archvios:")
        for f in archivos:
            print(f"    - {f}")
    
    input("\nPresiona enter para continuar...\n")


# -------------------------------------------------------------
#                  MENÚ PRINCIPAL
# -------------------------------------------------------------

def menu():
    while True:
        # Limpiar pantalla
        os.system("cls" if os.name == "nt" else "clear")
        
        
        print("\n+-----------------------------+")
        print("    ORGANIZADOR DE ARCHIVOS")
        print("         By: Dajachi")
        print("+-----------------------------+")
        
        print("\nOPCIONES:")
        print("\n1. Organizar")
        print("2. Listar")
        print("0. Salir")
        
        opcion = input("\nSelecciona una opción: ")
        
        
        # Opción 1 (Organizar archivos)
        if opcion == "1":
            
            # Pedir al usuario la ruta
            ruta = input("\nIngrese la ruta donde tienes los archivos: ")


            # Verificar si la ruta digitada por el usuario existe
            if os.path.exists(ruta):
                
                # Llamar a la función organizar_archivos
                organizar_archivos(ruta)

            else:
                print("\nLa ruta del directorio no existe.")
                sleep(1.5)
        
        
        # Opción 2 (Listador)
        elif opcion == "2":
            
            # Pedir al usuario la ruta
            ruta = input("\nIngrese la ruta donde tienes los archivos: ")


            # Verificar si la ruta digitada por el usuario existe
            if os.path.exists(ruta):
                
                # Llamar a la función listador
                listador(ruta)

            else:
                print("\nLa ruta del directorio no existe.")
                sleep(1.5)
            
        
        # Opción 0 (Salir)
        elif opcion == "0":
            print("\nGracias por utilizar el programa. ¡Hasta pronto!")
            sleep(2)
            break

        
        # Opción incorrecta
        else:
            print("\nEsa opción no existe...")
            sleep(1.5)


if __name__ == "__main__":
    menu()