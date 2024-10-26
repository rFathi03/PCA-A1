# PCA-A1
This repository demonstrates how to apply Principal Component Analysis (PCA) on images for dimensionality reduction, both for grayscale and RGB images. Additionally, we explore image compression by reducing a group of images into a smaller set containing common features (using the concept of eigenfaces).in the *Generative Adversarial Networks* course in FCAI-CU.


## Authors
- [Roaa Fathi](https://github.com/rFathi03)      
  

## Assignment Requirments
1. Apply PCA on a Grayscale Image.
2. Apply PCA on an RGB Image.
3. Compress a Group of Images Using Common Features (Eigenfaces).


## Task 1: Apply PCA on a Grayscale Image
### Steps:
- Convert the image into a matrix of pixel intensities.
- Perform PCA to extract the principal components.
- Reconstruct the image using a reduced number of components.
  
### Results
![Screenshot 2024-10-23 184856](https://github.com/user-attachments/assets/0aab74b2-abb6-4c15-8b1f-ffcdc1727ceb)

![Screenshot 2024-10-23 185056](https://github.com/user-attachments/assets/621158bc-605e-43b8-a9e5-d2383bda51cd)

## Task 2: Apply PCA on an RGB Image
### Steps:
- Split the image into its three color channels (R, G, B).
- Apply PCA to each channel independently to extract principal components.
- Reconstruct the image by combining the reduced channels.
  
### Results

![Screenshot 2024-10-23 185107](https://github.com/user-attachments/assets/24447deb-78d3-407a-8116-4423b1324ab4)

![Screenshot 2024-10-23 184909](https://github.com/user-attachments/assets/91e87faa-7cd8-4206-84c3-411f73b3a2f3)
## Task 3: Compress a Group of Images Using Common Features (Eigenfaces)
### Steps:
- Convert each image in the group into a vector.
- Perform PCA across the entire set of images.
- Identify and visualize the principal components (eigenfaces) that capture the most variance.
- Reconstruct into less number of images containing the common features using a combination of these eigenfaces.
### Results
![Screenshot 2024-10-26 194904](https://github.com/user-attachments/assets/7535d345-8b80-451a-97ac-e608bb0b575d)

![Screenshot 2024-10-26 194919](https://github.com/user-attachments/assets/852965e3-ddb4-4d26-8f75-f6295168a64a)

