# GAN Assingment 1 
# Name: Roaa Fathi
# ID: 20210140


import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


# ================================ PCA =====================================

def standardize(img):
    img_mean = np.mean(img, axis=0)
    centered_img = img - img_mean
    return centered_img, img_mean

def calc_cov(centered_img):
    img_cov_matrix = np.cov(centered_img, rowvar=False)
    return img_cov_matrix

def compute_eigen(cov_matrix):
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
    return eigenvalues, eigenvectors

def sort_eigen(eigenvalues, eigenvectors):
    sorted_idx = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[sorted_idx]
    sorted_eigenvectors = eigenvectors[:, sorted_idx]
    return sorted_eigenvalues, sorted_eigenvectors

def explained_variance(eigenvalues):
    total_variance = np.sum(eigenvalues)
    explained_variance = eigenvalues / total_variance
    cumulative_variance = np.cumsum(explained_variance)
    return cumulative_variance

def calculate_pc(cumulative_variance, variance_threshold):
    pc_num = np.argmax(cumulative_variance >= variance_threshold) + 1
    return pc_num

def project_data(centered_img, eigenvectors, pc_num):
    compressed_image = np.dot(centered_img, eigenvectors[:, :pc_num])
    return compressed_image

def PCA(img, variance_threshold=0.85):
    # Standardize the data
    centered_img, img_mean = standardize(img)

    # Calculate covariance matrix
    cov_matrix = calc_cov(centered_img)

    # Compute eigenvalues and eigenvectors
    eigenvalues, eigenvectors = compute_eigen(cov_matrix)

    # Sort eigenvalues and eigenvectors
    sorted_eigenvalues, sorted_eigenvectors = sort_eigen(eigenvalues, eigenvectors)

    # Compute explained variance
    cumulative_variance = explained_variance(sorted_eigenvalues)

    # Select number of principal components based on threshold
    pc_num = calculate_pc(cumulative_variance, variance_threshold)

    # Project data onto selected components
    compressed_image = project_data(centered_img, sorted_eigenvectors, pc_num)

    return compressed_image, sorted_eigenvectors[:, :pc_num], img_mean, pc_num

def decompress_image(compressed_img, eigenvectors, mean):
    # Image Reconstruction
    decompressed_image = np.dot(compressed_img, eigenvectors.T) + mean
    return decompressed_image


# ============================= Main Task ==================================

def run_grayscale():
    # Load the Grayscale Image
    image = cv2.imread('R:\Senior year\GAN\A1\Repo\PCA-A1\grayscale\eagleGS.jpg', cv2.IMREAD_GRAYSCALE)

    # Visualize the compressed and decompressed images
    plt.figure(figsize=(10,5))

    variance_threshold = 0.98

    compressed_img, eigen_vectors, mean, pc_num = PCA(image, variance_threshold)

    decompressed_img= decompress_image(compressed_img, eigen_vectors, mean)

    # Original image
    plt.subplot(1, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    # Compressed image
    plt.subplot(1, 3, 2)
    plt.imshow(compressed_img, cmap='gray')
    plt.title('Compressed Image')
    plt.axis('off')

    # Decompressed image
    plt.subplot(1, 3, 3)
    plt.imshow(decompressed_img, cmap='gray')
    plt.title('Decompressed Image')
    plt.axis('off')

    plt.show()

# ============================== Bonus 1 ===================================
def handle_shape(*channels, min_pc_num):
    return [channel[:, :min_pc_num] for channel in channels]



def run_RGB():
    # Load and convert image to RGB
    image = cv2.imread('R:\Senior year\GAN\A1\Repo\PCA-A1/RGB/lionRGB.jpg')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Split R, G, B channels
    channels = [image[:, :, i] for i in range(3)]
    variance_threshold = 0.98
    
    # Apply PCA to each channel
    compressed_channels = [PCA(channel, variance_threshold) for channel in channels]
    
    # Extract data from each channel
    compressed_data = [result[0] for result in compressed_channels]
    eigenvectors = [result[1] for result in compressed_channels]
    means = [result[2] for result in compressed_channels]
    pc_nums = [result[3] for result in compressed_channels]
    
    # Align the number of pc for all channels
    min_pc_num = min(pc_nums)
    compressed_channels_aligned = handle_shape(*compressed_data, min_pc_num=min_pc_num)
    
    # Full compression for all channels
    compressed_full = [project_data(channels[i] - means[i], eigenvectors[i], min_pc_num) for i in range(3)]
    
    # Stack compressed RGB channels
    compressed_image = np.stack(compressed_full, axis=2).astype(np.uint8)
    
    # Decompress each channel
    decompressed_channels = [decompress_image(compressed_full[i], eigenvectors[i][:, :min_pc_num], means[i]) for i in range(3)]
    
    # Stack decompressed channels to form the final image
    decompressed_image = np.stack(decompressed_channels, axis=2).astype(np.uint8)
    
    # Display images
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(image)
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(compressed_image)
    plt.title('Compressed Image')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(decompressed_image)
    plt.title('Decompressed Image')
    plt.axis('off')

    plt.show()


# ============================== Bonus 2 ===================================

def eigen_faces():
    pass

# ============================== Main App ==================================
def main_app():  
    run_grayscale()
    run_RGB()
    eigen_faces()

main_app()
