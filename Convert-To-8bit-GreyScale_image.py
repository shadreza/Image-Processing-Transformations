# import the image module

from PIL import Image

# Read a color image

colorImage = Image.open("parrots.png")

colorImage.show()

# Convert the color image to grey scale image

greyScaleImage = colorImage.convert("L")
# greyScaleImageOut = greyScaleImage.save("input1.png")
# display the grey scale image

greyScaleImage.show()

# convert the color image to black and white image

# blackAndWhiteImage = colorImage.convert("1")

# blackAndWhiteImage.show()

# Convert using adaptive palette of color depth 8

imageWithColorPalette = greyScaleImage.convert("P", palette=Image.ADAPTIVE, colors=8)
greyScale8BitImageOut = imageWithColorPalette.save("Input-Parrot-Greyscale-8bit-Image.png")
imageWithColorPalette.show()