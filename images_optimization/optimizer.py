import glob

from PIL import Image

from images_optimization.logger import logger

jpg_extensions = ['jpg', 'jpeg']
extensions = jpg_extensions + ['png', 'gif']

max_image_width = 3000
max_image_height = 3000


def optimize_images_from_directory(directory):
    for filename in glob.iglob('%s/*.*' % directory, recursive=True):
        filename_lower = filename.lower()
        is_image = any([filename_lower.endswith('.%s' % extension) for extension in extensions])
        is_jpg = any([filename_lower.endswith('.%s' % jpg_extension) for jpg_extension in jpg_extensions])

        if is_jpg:
            optimize_jpeg(filename)
        elif is_image:
            optimize_non_jpeg_image(filename)
        else:
            pass  # skip non-images


def optimize_jpeg(filename):
    logger.info('Optimizing « %s » with mozjpeg...' % filename)


def optimize_non_jpeg_image(filename):
    logger.info('Optimizing « %s » with Pillow...' % filename)

    try:
        image = Image.open(filename)
        image.thumbnail((max_image_width, max_image_height), Image.ANTIALIAS)
        image.save(filename, quality=80, optimize=True)
    except Exception:
        logger.exception('An error occurred during optimization with Pillow')
