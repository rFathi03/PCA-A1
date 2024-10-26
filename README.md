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
![Screenshot 2024-10-26 213224](https://github.com/user-attachments/assets/50dcfee7-aad6-4897-9629-28480b2268b6)


![Screenshot 2024-10-26 213424](https://github.com/user-attachments/assets/1574cf86-5837-4d66-8ebd-26bfd7691d24)

## Task 2: Apply PCA on an RGB Image
### Steps:
- Split the image into its three color channels (R, G, B).
- Apply PCA to each channel independently to extract principal components.
- Reconstruct the image by combining the reduced channels.
  
### Results
![Screenshot 2024-10-26 213238](https://github.com/user-attachments/assets/c583fb20-222d-440a-aa2c-2903b0bf7710)


![Screenshot 2024-10-26 213437](https://github.com/user-attachments/assets/93881339-2884-4029-8ec2-5b2aa470b51e)

## Task 3: Compress a Group of Images Using Common Features (Eigenfaces)
### Steps:
- Convert each image in the group into a vector.
- Perform PCA across the entire set of images.
- Identify and visualize the principal components (eigenfaces) that capture the most variance.
- Reconstruct into less number of images containing the common features using a combination of these eigenfaces.
### Results
![Screenshot 2024-10-26 213309](https://github.com/user-attachments/assets/d60c3c62-8675-4e6f-bd34-4d3226156891)


![Screenshot 2024-10-26 213324](https://github.com/user-attachments/assets/878528c0-5fe7-407b-8d31-69b505805b0f)
