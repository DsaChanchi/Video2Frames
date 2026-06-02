import cv2
import os

# Ruta del video
video_path = "video.mp4"

# Carpeta de salida
output_folder = "frames"
os.makedirs(output_folder, exist_ok=True)

# Abrir video
cap = cv2.VideoCapture(video_path)

frame_count = 0

while True:
    ret, frame = cap.read()

    # Si no hay más fotogramas
    if not ret:
        break

    # Nombre del archivo
    frame_filename = os.path.join(
        output_folder,
        f"frame_{frame_count:05d}.jpg"
    )

    # Guardar imagen
    cv2.imwrite(frame_filename, frame)

    frame_count += 1

print(f"Se guardaron {frame_count} fotogramas.")

cap.release()
