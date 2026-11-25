import hashlib
import shutil
from pathlib import Path

# Diccionario de categorías por extensión
CATEGORIAS = {
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp"],
    "Codigo": [".py", ".c", ".cpp", ".html", ".css", ".js", ".json"],
    "Comprimidos": [".zip", ".rar", ".tar", ".gz"],
}


def calcular_hash(ruta_archivo: Path) -> str:
    """Calcula la huella digital SHA-256 de un archivo para detectar duplicados exactos."""
    hasher = hashlib.sha256()
    with open(ruta_archivo, "rb") as f:
        # Leemos en bloques de 4KB para no saturar la RAM con archivos grandes
        for bloque in iter(lambda: f.read(4096), b""):
            hasher.update(bloque)
    return hasher.hexdigest()


def obtener_categoria(extension: str) -> str:
    """Devuelve la carpeta destino según la extensión del archivo."""
    ext = extension.lower()
    for categoria, extensiones in CATEGORIAS.items():
        if ext in extensiones:
            return categoria
    return "Otros"


def organizar_directorio(ruta_objetivo: str) -> None:
    directorio = Path(ruta_objetivo)
    if not directorio.exists() or not directorio.is_dir():
        print(f"Error: La ruta '{ruta_objetivo}' no es un directorio válido.")
        return

    hashes_vistos = set()
    movidos = 0
    duplicados = 0
    espacio_duplicado = 0

    for item in directorio.iterdir():
        # Ignorar carpetas y archivos ocultos (como .DS_Store)
        if item.is_dir() or item.name.startswith("."):
            continue

        huella = calcular_hash(item)

        # 1. Verificar si es duplicado por contenido real
        if huella in hashes_vistos:
            carpeta_dup = directorio / "Duplicados"
            carpeta_dup.mkdir(exist_ok=True)
            espacio_duplicado += item.stat().st_size
            shutil.move(str(item), str(carpeta_dup / item.name))
            duplicados += 1
            continue

        hashes_vistos.add(huella)

        # 2. Clasificar por categoría
        categoria = obtener_categoria(item.suffix)
        carpeta_destino = directorio / categoria
        carpeta_destino.mkdir(exist_ok=True)

        shutil.move(str(item), str(carpeta_destino / item.name))
        movidos += 1

    mb_ahorrados = espacio_duplicado / (1024 * 1024)
    print("\n--- Resumen de Organización ---")
    print(f"Archivos clasificados: {movidos}")
    print(f"Duplicados aislados:   {duplicados} ({mb_ahorrados:.2f} MB recuperables)")


if __name__ == "__main__":
    ruta = input("Ingresa la ruta de la carpeta a organizar (ej. ./carpeta_prueba): ").strip()
    organizar_directorio(ruta)