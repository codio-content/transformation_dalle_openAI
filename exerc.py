#CODIO SOLUTION BEGIN
import os
import openai
import secret
from PIL import Image,ImageOps
from io import BytesIO
import requests

openai.api_key = secret.api_key

# Generate the base image
def generate_base_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    return response['data'][0]['url']

cool_prompt= "Reunion of man, team, squad with katanas, ninja ,background forest , abstract, full hd render + 3d octane render +4k UHD + immense detail + dramatic lighting + well lit + black, purple, blue, pink, cerulean, teal, metallic colours, + fine details + octane render + 8k"
image_url = generate_base_image(cool_prompt)

img_data = requests.get(image_url).content
with open('cool.png', 'wb') as handler:
    handler.write(img_data)

#Saving our base image
base_image=Image.open('cool.png')
# Rotate the base image by 45 degrees
rotated_image_45 = base_image.rotate(45)

# Save the rotated image to a file
rotated_image_45.save('rotated_45_cool.png')

new_base= Image.open('rotated_45_cool.png')

# Invert the colors of the base image
inverted_image = ImageOps.invert(new_base)

# Save the inverted image to a file
inverted_image.save('final_cool.png')
#CODIO SOLUTION END