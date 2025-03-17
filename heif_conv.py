import os

import pillow_heif


# folders paths
input_folder = "HEIF"
output_folder = "PNG"

# creating output folder
os.makedirs(output_folder, exist_ok=True)

# CONVERTING HEIF
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".heic") or filename.lower().endswith(".heif"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.png")

        # opening HEIF image
        heif_file = pillow_heif.open_heif(input_path)
        image = heif_file.to_pillow()

        # saving as PNG with 70% original quality
        image.save(output_path, "PNG", quality=70)
        print(f"Converted: {filename} -> {output_path}")

print("Conversion completed!")
