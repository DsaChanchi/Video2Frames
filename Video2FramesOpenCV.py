import cv2
import os

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

    jpg_quality = int(
        input("Calidad JPG (0-100): ")
    )

elif format_option == "2":
    image_format = "png"

    png_compression = int(
        input("Compresión PNG (0-9): ")
    )

else:
    print("Opción inválida.")
    exit()

# =========================

os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)

fps = cap.get(cv2.CAP_PROP_FPS)

frame_interval = int(fps * interval_seconds)

frame_count = 0
saved_count = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    if frame_count % frame_interval == 0:

        frame_path = os.path.join(
            output_folder,
            f"frame_{saved_count:06d}.{image_format}"
        )

        # Guardar JPG
        if image_format == "jpg":

            cv2.imwrite(
                frame_path,
                frame,
                [cv2.IMWRITE_JPEG_QUALITY, jpg_quality]
            )

        # Guardar PNG
        elif image_format == "png":

            cv2.imwrite(
                frame_path,
                frame,
                [cv2.IMWRITE_PNG_COMPRESSION, png_compression]
            )

        saved_count += 1

    frame_count += 1

cap.release()

print(f"\nFrames guardados: {saved_count}")

    frame_count += 1

print(f"Se guardaron {frame_count} fotogramas.")

cap.release()
