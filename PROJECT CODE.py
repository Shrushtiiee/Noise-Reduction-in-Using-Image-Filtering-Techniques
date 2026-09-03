import cv2
from pathlib import Path
from tqdm import tqdm
import matplotlib.pyplot as plt

# Input folder
input_folder = "C:/Users/admin/Downloads/image_noise_dataset_25"

# Supported image formats
image_extensions = [".jpg", ".jpeg", ".png", ".bmp"]

# Get all images
image_files = []

for ext in image_extensions:
    image_files.extend(Path(input_folder).glob(f"*{ext}"))
    image_files.extend(Path(input_folder).glob(f"*{ext.upper()}"))

# Sort images
image_files = sorted(image_files)

print(f"Total images found: {len(image_files)}")

# USE ONLY FIRST 10 IMAGES
image_files = image_files[:10]

print(f"Processing only: {len(image_files)} images")

# Interactive display
plt.ion()

# Process images
for image_path in tqdm(image_files, desc="Processing Images"):

    # Read image
    image = cv2.imread(str(image_path))

    if image is None:
        continue

    # Convert BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Apply filters
    mean_filtered = cv2.blur(image_rgb, (5, 5))
    median_filtered = cv2.medianBlur(image_rgb, 5)
    gaussian_filtered = cv2.GaussianBlur(image_rgb, (5, 5), 0)

    # Clear previous figure
    plt.clf()

    # Display
    plt.figure(1, figsize=(15, 5))

    plt.subplot(1, 4, 1)
    plt.imshow(image_rgb)
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1, 4, 2)
    plt.imshow(mean_filtered)
    plt.title("Mean Filter")
    plt.axis("off")

    plt.subplot(1, 4, 3)
    plt.imshow(median_filtered)
    plt.title("Median Filter")
    plt.axis("off")

    plt.subplot(1, 4, 4)
    plt.imshow(gaussian_filtered)
    plt.title("Gaussian Filter")
    plt.axis("off")

    plt.suptitle(f"Image: {image_path.name}")

    plt.tight_layout()

    # Update display automatically
    plt.draw()
    plt.pause(1)

# Keep final image visible
plt.ioff()
plt.show()

print("Processing Completed Successfully!")
