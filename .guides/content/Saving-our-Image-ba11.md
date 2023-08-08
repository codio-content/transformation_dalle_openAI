
### Image Generation
---
In order to not have to keep copying and pasting our result in, we are going to save the image so that we can interact with as a file in our Codio box. 

The first thing we are going to do is get our base image. Previously we used very simple prompts to generate simple images. The simple images were very useful to see the color transformations. Now that we are going to work with more spacial transformations we can make some cooler pictures and still easily visualize the changes. Let's start with getting our library and image generation function

```python
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
```
{Try it!}(python3 imageGen.py 1)

From there you can use any prompt you would like. We are going to use the following prompt:
```python
cool_prompt= "Reunion of man, team, squad with katanas, cyberpunk, abstract, full hd render + 3d octane render +4k UHD + immense detail + dramatic lighting + well lit + black, purple, blue, pink, cerulean, teal, metallic colours, + fine details + octane render + 8k"

image_url = generate_base_image(cool_prompt)

img_data = requests.get(image_url).content
with open('base_img.jpg', 'wb') as handler:
    handler.write(img_data)
```
{Try it!}(python3 imageGen.py 2)
[Click here to refresh your image](close_file base_img.jpg panel=1; open_file base_img.jpg panel=1) 


In our case the following prompt generated this pretty cool image. 
![base_Img](base_Img0.jpg)

**If** you want feel free to generate other images until you have something you like. **If** you want to use the picture above, you can run the following code. Additional images will be provided below, if you want them simply switch the corresponding source file. Example, `base_img9.jpg` or `base_img8.jpg` ... Please remember to comment out the code to generate a new image.

```python
import shutil

# Set the source and destination file paths
src_file = "base_Img0.jpg"
dst_file = "base_img.jpg"

# Copy the file to the new destination
shutil.copy(src_file, dst_file)
```
{Try it!}(python3 imageGen.py 3)
[Click here to refresh your image](close_file base_img.jpg panel=1; open_file base_img.jpg panel=1) 

Comment out the code so you are no longer generating and moving your files. More choices are available including their prompts below:

### img9
```python
cool_prompt= "cybernetic ninja cyborg with glowing parts , ninja has sword, impressive, surreal, cinematic lighting, cinematic photoshot, extremely detailed and complex, VFX volume fog around, nighttime, super max, surreal, super detailed, high contrast, Rtx on, Hdr, photography, realistic, dof on, fov on, motion blur, lens flares on, 50mm Prime f/1.8, White balance, Super resolution, Megapixel, ProPhoto RGB, VR, high, epic, Rear half lighting, Lights background, natural lighting, incandescent light, fiber optic, mood lighting, cinema lighting, studio lighting, soft illumination, volumetric, contrast, dark lighting, accent lighting, projection global illumination, Screen space global illumination, Ray tracing global illumination, Red fringing light, 45% cold color grading, Optics, Scattering, Glow, Shadows, hyperrealism, Caustic water, refraction water, exquisite detail, intricately-detailed, ultra-detailed photography, high-sharpness, high reflection, award-winning photograph"
```
![base_img9](base_img9.jpg)

### img8
```python
cool_prompt= " masked mutant with  fire powers,  standing atop a skyscraper during a thunderstorm. body is crackling with electricity, with glowing veins and eyes. cyberpunk, abstract, full hd render + 3d octane render +4k UHD + immense detail + dramatic lighting + well lit + black, purple, blue, pink, cerulean, teal, metallic colours + fine details + octane render + 8k"
```
![base_img8](base_img8.jpg)

### img7
```
cool_prompt="Create an image of a futuristic city with towering skyscrapers, advanced transportation systems, and renewable energy sources. Use high-tech materials that shimmer and reflect light, and incorporate green spaces and parks into the skyline. Use dynamic and colorful lighting with neon lights and holographic projections. Show a diverse and cosmopolitan population with cutting-edge fashion and technology. Capture the city's sleek and sophisticated aesthetic in your image."
```

![base_img7](base_img7.jpg)