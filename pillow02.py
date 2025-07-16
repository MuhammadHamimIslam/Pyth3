from PIL import Image, ImageFilter


img = Image.open("templates/beautiful_img.jpg") # opens the image file

# image manipulation
transposed_img = img.transpose(Image.FLIP_TOP_BOTTOM)
# there're 7 arguments to pass
# 1. Image.FLIP_LEFT_RIGHT
# 2. Image.FLIP_TOP_BOTTOM
# 3. Image.ROTATE_90
# 4. Image.ROTATE_180
# 5. Image.ROTATE_270
# 6. Image.TRANSPOSE
# 7. Image.TRANSVERSE
transposed_img.save("transposed_img.jpg")

# rotating an image
rotated_img = img.rotate(45, expand=True) # rotates 45 degree, expands so that nothing is being cropped
rotated_img.save("rotated_img.jpg")

# convert image's band
grayscale_img = img.convert("L") # converts to grayscale
# "L" -> grayscale
# "RGB" -> rgb
# "CMYK" -> cmyk
grayscale_img.save("grayscale_img.jpg")

# Separeting bands of an image
red, green, blue = img.split() # splits into red, green, blue

# merging bands
zeroed_band = red.point(lambda _: 0) # zero the band

red_merge = Image.merge(
    "RGB", (red, zeroed_band, zeroed_band)
) # merge to red
green_merge = Image.merge(
    "RGB", (zeroed_band, green, zeroed_band)
) # merge to green
blue_merge = Image.merge(
    "RGB", (zeroed_band, zeroed_band, blue)
) # merge to blue

red_merge.save("red_merge.jpg")
green_merge.save("green_merge.jpg")
blue_merge.save("blue_merge.jpg")

# filtering image

# bluring an image
blured_img = img.filter(ImageFilter.BLUR)
blured_img.save("blured_img.jpg")

# bluring with specific value with ImageFilter.BoxBlur() or ImageFilter.GaussianBlur()
blured_15_img = img.filter(ImageFilter.BoxBlur(15)) # blur with value 15
blured_15_img.save("blured_15_img.jpg")

gaussian_blur_img = img.filter(ImageFilter.GaussianBlur(15))
gaussian_blur_img.save("gaussian_blur_img.jpg")

# sharpen an image
sharpen_img = img.filter(ImageFilter.SHARPEN)
sharpen_img.save("sharpen_img.jpg")

# smoothen an image
smooth_img = img.filter(ImageFilter.SMOOTH)
smooth_img.save("smooth_img.jpg")

# finding edges
img_gray = img.convert("L") # convert to grayscale first
edges = img_gray.filter(ImageFilter.FIND_EDGES) # find edges
edges.save("edges.jpg")

# detecting edges after making smooth
img_gray_smooth = img.filter(ImageFilter.SMOOTH) # makes the grayscale image to smooth
edges_smooth = img_gray_smooth.filter(ImageFilter.FIND_EDGES) # now find edges
edges_smooth.save("edges_smooth.jpg")

# enhance edged
edges_smooth_enhance = edges_smooth.filter(ImageFilter.EDGE_ENHANCE)
edges_smooth_enhance.save("edges_smooth_enhance.jpg")

# ImageFilter.EMBOSS
emboss = img_gray_smooth.filter(ImageFilter.EMBOSS)
emboss.save("emboss.jpg")