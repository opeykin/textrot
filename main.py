__author__ = 'alex'

from PIL import Image, ImageDraw

from routines import draw_word


width = 640
height = 480
word = "ALGEBRA"

img = Image.new("RGB", (width, height), "black")
draw = ImageDraw.Draw(img)

draw_word(word, 2, width, height, draw, "white")

img.save("img.png", "PNG")
