from PIL import Image, ImageFilter

# Image Thresholding
cat_img = Image.open("templates/cat_img.jpg") # open tje cat image

cat_img = cat_img.crop((400, 100, 830, 600)) # crop the image to get the cat only

cat_img_gray = cat_img.convert("L") # make it grayscale
threshold = 110 # set threshold
cat_img_threshold = cat_img_gray.point(
    lambda x: 255 if x > threshold else 0
) # make threshold image

# image erosion
def erode(cycle, image):
    for _ in range(cycle):
        image = image.filter(ImageFilter.MinFilter(3))
    return image
# image dialation
def dialate(cycle, image):
    for _ in range(cycle):
        image = image.filter(ImageFilter.MaxFilter(3))
    return image

step_1 = erode(6, cat_img_threshold) # erode the image
step_2 = dialate(15, step_1)
cat_mask = erode(9, step_2)

cat_mask = cat_mask.convert("L")
cat_mask = cat_mask.filter(ImageFilter.BoxBlur(20))

blank = cat_img.point(lambda _: 0)
cat_segment = Image.composite(cat_img, blank, cat_mask)

# Superimposition of Images Using Image.paste()
monastery_img = Image.open("templates/monastery.jpg")

monastery_img.paste(
    cat_img.resize((cat_img.width // 4, cat_img.height // 4)),
    (600, 450),
    cat_mask.resize((cat_mask.width // 4, cat_mask.height // 4))
)
monastery_img.save("monastery_cat.jpg")