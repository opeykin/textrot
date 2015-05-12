__author__ = 'alex'
import Image
import ImageDraw

from routines import draw_word


width = 300
height = 100
word = "FUCK"

img = Image.new("RGB", (width, height), "black")
draw = ImageDraw.Draw(img)

draw_word(word, 2, width, height, draw, "white")

img.save("img.png", "PNG")