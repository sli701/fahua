import os
from PIL import Image, ImageOps

# Folder containing images
input_folder = ".\\fa_app\\img_raw"
output_folder = ".\\fa_app\\img_trim"

os.makedirs(output_folder, exist_ok=True)

os.makedirs(output_folder, exist_ok=True)

target_size = (400, 400)  # Max width, height

for file in os.listdir(input_folder):
    if file.lower().endswith(('.png', '.jpg', '.jpeg')):
        img_path = os.path.join(input_folder, file)
        img = Image.open(img_path)

        # Resize keeping aspect ratio
        img.thumbnail(target_size, Image.LANCZOS)

        # Save resized image
        img.save(os.path.join(output_folder, file))

print("✅ All images resized (aspect ratio preserved)!")

