# Noise Reduction Using Image Filtering Techniques

## 📌 Project Description

Image noise is an unwanted variation in pixel values that can reduce the quality and clarity of an image. Noise may occur during image acquisition, transmission, compression, or due to limitations in camera sensors. In the field of Computer Vision and Digital Image Processing, noise reduction is an important preprocessing step because clean images improve the performance of further image analysis tasks.

This project focuses on applying different image filtering techniques to reduce noise in a collection of images. Instead of processing only a single image, the project is designed to handle multiple images from an image dataset automatically. This demonstrates a scalable approach to image processing and introduces the concept of batch processing.

The project uses Python and the OpenCV library to read images and apply three commonly used noise reduction filters:

- Mean Filter
- Median Filter
- Gaussian Filter

Each image is processed individually, and the results of all three filters are compared with the original image. For visualization purposes, the program selects the first 10 images from the dataset and displays them automatically on the screen.

For every selected image, four versions are displayed:

1. Original Image
2. Mean Filtered Image
3. Median Filtered Image
4. Gaussian Filtered Image

This allows users to visually compare the effectiveness of different filtering techniques and understand how each filter affects image smoothness, noise reduction, and edge preservation.

The project is useful for understanding the practical implementation of image preprocessing techniques and demonstrates how Python can be used to process multiple images efficiently.

---

## 🎯 Objective

The main objective of this project is to perform noise reduction on multiple images using different image filtering techniques and compare their results.

The project aims to achieve the following objectives:

### 1. Process Multiple Images Automatically

Instead of manually selecting and processing individual images, the program automatically identifies all supported images available in the dataset folder.

This makes the system suitable for handling datasets containing multiple images.

---

### 2. Apply Different Noise Reduction Filters

The project applies three different filtering techniques to every selected image:

- Mean Filter
- Median Filter
- Gaussian Filter

Each filter uses a different approach to reduce noise.

---

### 3. Compare Filtering Techniques

The results produced by each filtering method are displayed alongside the original image.

This visual comparison helps in understanding:

- How much noise is removed
- How much image detail is preserved
- Whether image edges become blurred
- Which filter performs better for different types of noise

---

### 4. Understand Image Preprocessing

Image preprocessing is an important stage in Computer Vision and Machine Learning applications.

This project demonstrates how raw or noisy images can be processed before performing tasks such as:

- Object Detection
- Image Classification
- Face Recognition
- Medical Image Analysis
- Pattern Recognition
- Machine Learning

---

### 5. Demonstrate Batch Processing

The project demonstrates how multiple images can be processed using a loop.

Instead of writing separate code for each image, the program automatically performs the same operations on multiple images.

This approach is useful when working with larger datasets.

---

### 6. Handle Large Image Datasets Efficiently

The program is designed to identify multiple images from a dataset folder.

Although the dataset may contain many images, only 10 images are selected for visualization. This improves execution speed and prevents excessive memory usage while still demonstrating large dataset processing.

---

## 🛠 Technologies Used

The following technologies and Python libraries are used in this project:

### 1. Python

Python is the main programming language used to develop this project.

It is widely used in:

- Data Science
- Machine Learning
- Artificial Intelligence
- Computer Vision
- Image Processing

Python provides simple syntax and powerful libraries for image analysis.

---

### 2. OpenCV

OpenCV stands for Open Source Computer Vision Library.

It is used in this project for:

- Reading images
- Image processing
- Color conversion
- Applying Mean Filter
- Applying Median Filter
- Applying Gaussian Filter

The following OpenCV functions are used:

```python
cv2.imread()
