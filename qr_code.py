import qrcode

url = "color-pulse.pages.dev"
qr = qrcode.make(url)
qr.save("color-pulse.png")

# adding more data for url

data = input("Enter the url to generate QR Code: ")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
) # qrcode configuration 

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="white", back_color="black") # setting color
img.save("qr.png") # save the image 