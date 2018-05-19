from PIL import Image

max_image_width = 3000
max_image_height = 3000


def optimize(filename):
    image = Image.open(filename)
    image.thumbnail((max_image_width, max_image_height), Image.ANTIALIAS)
    image.save(filename, quality=80, optimize=True)
