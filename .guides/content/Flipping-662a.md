Flipping an image involves mirroring it either horizontally or vertically. This can be useful for creating reflections, correcting image orientation, or generating additional variations of a generated image.  we will explore horizontal and vertical flipping using the Python Imaging Library (PIL) and the DALL-E 2 API.


### Horizontal Flipping

Horizontal flipping mirrors the image along its vertical axis, effectively reversing its left and right sides. This can be used to create a reflection effect or to correct an image's orientation if it appears reversed. Now feel free to comment out the code from the previous page, remember to keep your libraries. After copy and paste the following code. 

```python 
#Saving our base image
base_image=Image.open('base_img.jpg')
# Flip the base image horizontally
flipped_horizontal_image = ImageOps.mirror(base_image)

# Save the horizontally flipped image to a file
flipped_horizontal_image.save('flipped_horizontal.jpg')
```
{Try it!}(python3 imageGen.py 4)
[Click here to refresh your horizontal image](close_file flipped_horizontal.jpg panel=1; open_file flipped_horizontal.jpg panel=1) 

The base image is provided in that same lower left panel so it's easy to compare. 

### Vertical Flipping

Vertical flipping mirrors the image along its horizontal axis, effectively reversing its top and bottom sides. This can be useful for creating a reflection effect on a horizontal surface or correcting an image's orientation if it appears upside-down.

```python
# Flip the base image vertically
flipped_vertical_image = ImageOps.flip(base_image)

# Save the vertically flipped image to a file
flipped_vertical_image.save('flipped_vertical.jpg')
```
{Try it!}(python3 imageGen.py 5)
[Click here to refresh your vertical  image](close_file flipped_vertical.jpg panel=1; open_file flipped_vertical.jpg panel=1)

### Combining Flips

You can also combine horizontal and vertical flips to create a diagonal reflection effect or generate additional variations of the image.

```python
# Flip the base image horizontally and vertically
flipped_both_image = ImageOps.mirror(ImageOps.flip(base_image))

# Save the horizontally and vertically flipped image to a file
flipped_both_image.save('flipped_both.jpg')
```
{Try it!}(python3 imageGen.py 6)
[Click here to refresh your vertical  image](close_file flipped_both.jpg panel=1; open_file flipped_both.jpg panel=1)


{Check It!|assessment}(fill-in-the-blanks-896389336)
