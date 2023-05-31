Rotating an image involves changing its orientation by a specified angle. This can be useful for correcting image orientation, creating dynamic compositions, or generating additional variations of a generated image. In this extended example, we will explore various ways to rotate images using the Python Imaging Library (PIL) and the DALL-E 2 API. To avoid clutter we are going to use a new code file. Since we know where our base image is located we just need our libraries.
```python
import os
import openai
import secret
from PIL import Image,ImageOps
from io import BytesIO
import requests

openai.api_key = secret.api_key

#Saving our base image
base_image=Image.open('base_img.jpg')
```


### Basic Rotation

In its simplest form, image rotation involves specifying an angle by which to rotate the image. The image is rotated around its center by default.
```python
# Rotate the base image by 45 degrees
rotated_image_45 = base_image.rotate(45)

# Save the rotated image to a file
rotated_image_45.save('rotated_45_.jpg')
```

{Try it!}(python3 ImageGen2.py 1)
[Click here to refresh your rotate image](close_file rotated_45_.jpg panel=1; open_file rotated_45_.jpg panel=1) 

### Rotation with Resampling

When rotating an image, the original pixel values may not align with the new pixel grid. To address this issue, you can use resampling techniques, which interpolate the pixel values to create a smoother appearance. The most common resampling technique is bilinear interpolation.
```python
# Rotate the base image by 45 degrees with bilinear interpolation
rotated_image_45_bilinear = base_image.rotate(45, resample=Image.BILINEAR)

# Save the rotated image with bilinear interpolation to a file
rotated_image_45_bilinear.save('rotated_45_bilinear.jpg')
```
{Try it!}(python3 ImageGen2.py 2)
[Click here to refresh your rotate image](close_file rotated_45_bilinear.jpg panel=1; open_file rotated_45_bilinear.jpg panel=1) 

### Rotation with Custom Center


By default, the image is rotated around its center. However, you can specify a custom center for the rotation if you want to create a different effect or composition

```python
# Define custom center coordinates (x, y)
center_x = 100
center_y = 100

# Rotate the base image by 45 degrees around the custom center
rotated_image_custom_center = base_image.rotate(45, center=(center_x, center_y))

# Save the rotated image with custom center to a file
rotated_image_custom_center.save('rotated_custom_center.jpg')
```
{Try it!}(python3 ImageGen2.py 2)
[Click here to refresh your rotate image](close_file rotated_custom_center.jpg panel=1; open_file rotated_custom_center.jpg panel=1) 


### Rotation with Expand Option

When rotating an image, the corners may be cropped if they extend beyond the original image boundaries. To avoid this, you can use the expand option to automatically resize the image canvas to accommodate the rotated image.

```python
# Rotate the base image by 120 degrees and expand the canvas
rotated_image_expanded = base_image.rotate(120, expand=True)

# Save the rotated image with expanded canvas to a file
rotated_image_expanded.save('rotated_expanded.jpg')
```
{Try it!}(python3 ImageGen2.py 3)
[Click here to refresh your rotate image](close_file rotated_expanded.jpg panel=1; open_file rotated_expanded.jpg panel=1)

By applying various rotation techniques to images generated by the DALL-E 2 API, you can create interesting and dynamic compositions, adding visual appeal and diversity to your images.


{Check It!|assessment}(multiple-choice-1236741021)

