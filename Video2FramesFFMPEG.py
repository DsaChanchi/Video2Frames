import os
import subprocess

# =========================
# CONFIGURACIÓN INTERACTIVA
# =========================

video_path = input("Ruta del video: ")
output_folder = input("Carpeta de salida: ")

# Tiempo entre frames
interval_seconds = float(
    input("Cada cuántos segundos extraer un frame: ")
)

# Elegir formato
print("\nFormato de imagen:")
print("1 - JPG")
print("2 - PNG")

format_option = input("Elige una opción (1/2): ")

if format_option == "1":

    image_format = "jpg"

    jpg_quality = input(
        "Calidad JPG (1-31, donde 1 es máxima calidad): "
    )

elif format_option == "2":

    image_format = "png"

    png_compression = input(
        "Compresión PNG (0-9, donde 0 es máxima calidad): "
    )

else:
    print("Opción inválida.")
    exit()

# =========================

os.makedirs(output_folder, exist_ok=True)

output_pattern = os.path.join(
    output_folder,
    f"frame_%06d.{image_format}"
)

# Construir comando FFmpeg
command = [
    "ffmpeg",
    "-hide_banner",
    "-loglevel", "error",
    "-i", video_path,
    "-vf", f"fps=1/{interval_seconds}"
]

# Calidad JPG
if image_format == "jpg":

    command.extend([
        "-q:v", str(jpg_quality)
    ])

# Compresión PNG
elif image_format == "png":

    command.extend([
        "-compression_level",
        str(png_compression)
    ])

# Archivo de salida
command.append(output_pattern)

# Ejecutar FFmpeg
try:

    subprocess.run(command, check=True)

    print("\nFrames extraídos correctamente.")

except subprocess.CalledProcessError:

    print("\nError ejecutando FFmpeg.")
