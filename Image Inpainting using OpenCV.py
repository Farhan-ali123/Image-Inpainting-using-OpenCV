import numpy as np
import cv2

# Open the image.
img = cv2.imread('C:\\Users\\user\\Desktop\\newp\\venv\\resources\\ct.png')

# Load the mask.
mask = cv2.imread('C:\\Users\\user\\Desktop\\newp\\venv\\resources\\cm.png', 0)

# Inpaint.
dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)

# Write the output.
cv2.imwrite('cat_inpainted.png', dst)
