# -*- coding: utf-8 -*-
"""ImageClear_New.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dNqS4_-J2hvaGOJwiy0_SXh8o7SV9YN3
"""

import numpy as np
from skimage import io, img_as_float
import imquality.brisque as brisque

import cv2
import numpy as np

# load the grayscale image
img_gray = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# create a color image with three channels
img_color = np.zeros((img_gray.shape[0], img_gray.shape[1], 3), dtype=np.uint8)

# copy the grayscale image to all three channels
img_color[:, :, 0] = img_gray
img_color[:, :, 1] = img_gray
img_color[:, :, 2] = img_gray

# now you can apply the operation that expects a color image

img = img_as_float(io.imread('image.jpg')[:,:,:3])
# img1 = img_as_float(io.imread('clr_img.jpg',as_gray=True))

import cv2
from skimage.metrics import structural_similarity as ssim

def check_image_quality(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Unable to read the image file")
        return

    # Calculate the image quality using the Structural Similarity Index (SSIM)
    # The higher the SSIM score, the better the quality of the image.
    ssim_score = ssim(img, img, multichannel=True)
    print(ssim_score)
    if ssim_score > 0.8:
        print("The image quality is good")
    else:
        print("The image quality is poor")

check_image_quality("clr_img.jpg")

import cv2

def variance_of_laplacian(image):
    # convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # apply the Laplacian operator
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    # calculate the variance of the Laplacian
    variance = laplacian.var()
    return variance

# load the image
image = cv2.imread('image.jpg')

# calculate the variance of the Laplacian
variance = variance_of_laplacian(image)

# define a threshold value for the variance
threshold = 100

# check if the variance is below the threshold
if variance < threshold:
    print("Image is blurry") 
else:
    print("Image is not blurry")
