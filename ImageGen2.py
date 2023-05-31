# CODIO SOLUTION BEGIN
import os
import openai
import secret
from PIL import Image,ImageOps
from io import BytesIO
import requests

openai.api_key = secret.api_key

#Saving our base image
base_image=Image.open('base_img.jpg')
# Rotate the base image by 45 degrees
rotated_image_45 = base_image.rotate(45)

# Save the rotated image to a file
rotated_image_45.save('rotated_45_.jpg')

from PIL import Image
# Rotate the base image by 45 degrees with bilinear interpolation
rotated_image_45_bilinear = base_image.rotate(75, resample=Image.BILINEAR)

# Save the rotated image with bilinear interpolation to a file
rotated_image_45_bilinear.save('rotated_45_bilinear.jpg')

# Define custom center coordinates (x, y)
center_x = 100
center_y = 100

# Rotate the base image by 45 degrees around the custom center
rotated_image_custom_center = base_image.rotate(45, center=(center_x, center_y))

# Save the rotated image with custom center to a file
rotated_image_custom_center.save('rotated_custom_center.jpg')

# Rotate the base image by 120 degrees and expand the canvas
rotated_image_expanded = base_image.rotate(120, expand=True)

# Save the rotated image with expanded canvas to a file
rotated_image_expanded.save('rotated_expanded.jpg')
# CODIO SOLUTION END