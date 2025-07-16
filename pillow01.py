from PIL import Image, ImageFilter


# first open the image
img = Image.open("templates/beautiful_img.jpg") # opens the image file

# get image info
print(img.format) # image format
print(img.size) # image size
print(img.mode) # image mode
print(img.getbands()) # image bands (e.g. RGB, CMYK, etc)

# changing file extension
img.save("beautiful_img.png") # saves the jpg image as png

# crop an image
# image.crop((tuple)) : 4-tuple defining the left, upper, right, and lower pixel 
cropped_img = img.crop((50, 20, 150, 150)) # crops images taking 50 pixel from left, 20 from upper, 150 pixel from right and 150 pixel from bottom
cropped_img.save("cropped_img.jpg")

# resizing an image
# image.resize(width, height)
resized_img = cropped_img.resize((300, 300)) # resizes image with width and height to 300, 300 px
resized_img.save("resized_img.jpg")

# Erosion and Dilation
dot_hole = Image.open("templates/dot_and_hole.jpg") # The left-hand side of this binary image shows a white dot on a black background, while the right-hand side shows a black hole in a solid white section
# Erosion is the process of removing white pixels from the boundaries in an image
# ImageFilter.MinFilter(3)
for _ in range(3):
    erosion = dot_hole.filter(ImageFilter.MinFilter(3))
erosion.save("erosion.jpg")

# Dilation is the opposite process to erosion. White pixels are added to the boundaries in a binary image
# ImageFilter.MaxFilter(3)
for _ in range(3):
    dilation = dot_hole.filter(ImageFilter.MaxFilter(3))
dilation.save("dilation.jpg")

# dilation and erosion together
for _ in range(17):
    erosion_dilation = dot_hole.filter(ImageFilter.MinFilter(3))
for _ in range(17):
    erosion_dilation = erosion_dilation.filter(ImageFilter.MaxFilter(3))

erosion_dilation.save("erosion_dilation.jpg")