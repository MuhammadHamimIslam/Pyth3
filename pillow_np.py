from PIL import Image
import numpy as np

# image manipulatuon with numpy
house1 = Image.open("templates/house1.jpg")
house2 = Image.open("templates/house2.jpg")

house1_array = np.asarray(house1) # house1 array
house2_array = np.asarray(house2) # house2 array
difference_array = house1_array - house2_array # difference array

difference_img = Image.fromarray(difference_array)

# using numpy to create image
square = np.zeros((600, 600), dtype=np.uint8) # 600x600 array
square[200:400, 200:400] = 255 # place black square at the center
square_img = Image.fromarray(square)
square_img.save("square_img.jpg")

# make red, green, blue section
red = np.zeros((600, 600))
green = np.zeros((600, 600))
blue = np.zeros((600, 600))
red[150:350, 150:350] = 255
green[200:400, 200:400] = 255
blue[250:450, 250:450] = 255

red_img = Image.fromarray(red).convert("L")
green_img = Image.fromarray(green).convert("L")
blue_img = Image.fromarray((blue)).convert("L")

colored_img = Image.merge("RGB", (red_img, green_img, blue_img))
colored_img.save("colored_img.jpg")

# creating animation (gif)
square_animation = []

for offset in range(0, 100, 2):  # loop 50 times
    red = np.zeros((600, 600))
    green = np.zeros((600, 600))
    blue = np.zeros((600, 600))
    
    red[101 + offset : 301, 101 + offset :  301] = 255
    green[200:400, 200:400] = 255
    blue[299 - offset : 499 - offset, 299 - offset : 499 - offset] = 255
    
    red_img = Image.fromarray((red)).convert("L")
    green_img = Image.fromarray((green)).convert("L")
    blue_img = Image.fromarray((blue)).convert("L")
    
    square_animation.append(
        Image.merge("RGB", (red_img,green_img, blue_img))
    )

square_animation[0].save(
    "animation.gif", save_all=True, append_images=square_animation[1:]
)