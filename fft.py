#!/usr/bin/python3

import cv2, sys
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) != 2:
  print("Image FFT Proccessing")
  print("   Usage: ./fft.py <filename>")
else:
  # Get file input
  file = sys.argv[1]

 # Process Image
  img_c1 = cv2.imread(file, 0) # Original Image
  img_c2 = np.fft.fft2(img_c1)                # Spectrum
  img_c3 = np.fft.fftshift(img_c2)            # Centered Spectrum
  img_c4 = np.fft.ifftshift(img_c3)           # Decentralized
  img_c5 = np.fft.ifft2(img_c4)               # Processed Image

 # Plot Image FFTs
  plt.subplot(234), plt.imshow(img_c1,                   "gray"), plt.title("Original")
  plt.subplot(231), plt.imshow(np.log(1+np.abs(img_c2)), "gray"), plt.title("Spectrum")
  plt.subplot(232), plt.imshow(np.log(1+np.abs(img_c3)), "gray"), plt.title("Centered Spectrum")
  plt.subplot(233), plt.imshow(np.log(1+np.abs(img_c4)), "gray"), plt.title("Decentralized")
  plt.subplot(236), plt.imshow(np.abs(img_c5),           "gray"), plt.title("Processed Image")

  # Display Plot
  plt.show()
