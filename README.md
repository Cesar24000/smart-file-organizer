# Smart File Organizer & Duplicate Detector

Herramienta de línea de comandos (CLI) desarrollada en Python para automatizar la organización de directorios y detectar archivos duplicados mediante verificación criptográfica de contenido.

## Características principales

* **Detección exacta de duplicados (SHA-256):** Calcula la huella digital de cada archivo leyendo en bloques binarios de 4 KB para evitar saturar la memoria RAM, incluso con archivos pesados. Indexa los hashes en un `set` para detectar duplicados en tiempo constante ($O(1)$) sin importar el nombre o la extensión del archivo.
* **Aislamiento seguro:** Mueve los archivos duplicados a una carpeta `Duplicados/` en lugar de eliminarlos permanentemente, calculando y reportando el espacio total recuperable en megabytes.
* **Clasificación automática por extensión:** Organiza los archivos en categorías predefinidas (`Documentos`, `Imagenes`, `Codigo`, `Comprimidos`, `Otros`) utilizando `pathlib` y `shutil`.
* **Protección de archivos del sistema:** Ignora subdirectorios existentes y archivos ocultos (como `.DS_Store` en macOS) para evitar alterar configuraciones del entorno.

## Tecnologías utilizadas

* **Python 3** (100% librerías estándar, sin dependencias externas):
  * `pathlib` — Manejo moderno de rutas y directorios multiplataforma.
  * `hashlib` — Generación de hashes criptográficos SHA-256.
  * `shutil` — Movimiento seguro de archivos entre directorios.

## Estructura del proyecto

```text
smart-file-organizer/
├── organizer.py       # Lógica principal de clasificación y hashing SHA-256
├── README.md          # Documentación del proyecto
└── .gitignore         # Exclusión de archivos temporales y de sistema
```

## Cómo ejecutarlo

1. Clona este repositorio en tu equipo:
   ```bash
   git clone https://github.com/Cesar24000/smart-file-organizer.git
   ```
2. Entra al directorio del proyecto:
   ```bash
   cd smart-file-organizer
   ```
3. Ejecuta el script:
   ```bash
   python3 organizer.py
   ```
4. Ingresa la ruta del directorio que deseas organizar cuando la terminal lo solicite (por ejemplo: `./carpeta-prueba`).

## Ejemplo de salida en consola

```text
Ingresa la ruta de la carpeta a organizar (ej. ./carpeta_prueba): ./carpeta-prueba

--- Resumen de Organización ---
Archivos clasificados: 2
Duplicados aislados:   3 (0.00 MB recuperables)
```

---
Desarrollado por **César Alejandro Aguayo Gómez** — Estudiante de Ingeniería en Desarrollo de Software (ITESO)