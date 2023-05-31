#CODIO SOLUTION BEGIN
import os
import openai
import secret
from PIL import Image,ImageOps
from io import BytesIO
import requests

openai.api_key = secret.api_key

#Saving our base image
base_image=Image.open('base_img.jpg')

# Invert the colors of the base image
inverted_image = ImageOps.invert(base_image)

# Save the inverted image to a file
inverted_image.save('inverted.jpg')

# Convert the base image to grayscale
grayscale_image = ImageOps.grayscale(base_image)

# Invert the grayscale image
inverted_grayscale_image = ImageOps.invert(grayscale_image)

# Save the inverted grayscale image to a file
inverted_grayscale_image.save('inverted_grayscale.jpg')


# Split the color channels of the base image
r, g, b = base_image.split()

# Invert the red and green channels
#inverted_r = ImageOps.invert(r)
inverted_g = ImageOps.invert(g)

# Combine the inverted red and green channels with the original blue channel


# Save the custom channel inverted image to a file
inverted_g.save('inverted_custom_channels.jpg')

#CODIO SOLUTION END