import glob

from PIL import Image

from images_optimization import mozjpeg
from images_optimization.logger import logger
from images_optimization.args_parser import parse_args
from images_optimization.permissions_fixer import fix_permissions

jpg_extensions = ['jpg', 'jpeg']
extensions = jpg_extensions + ['png', 'gif']

max_image_width = 3000
max_image_height = 3000


def optimize_images_from_directory(directory):
    for filename in _list_filenames(directory):
        _optimize_image(filename)


def _list_filenames(directory):
    logger.info('Listing files...')

    filenames = glob.glob('%s/*.*' % directory, recursive=True)
    filenames = sorted(filenames)

    after_filename = parse_args().after

    if after_filename:
        after_filename = '%s/%s' % (directory, after_filename)

        try:
            after_filename_position = filenames.index(after_filename)
            filenames = filenames[after_filename_position + 1:]
        except ValueError:
            logger.error('Filename « %s » do not exists.' % after_filename)
            exit(1)

    return filenames


def _optimize_image(filename):
    filename_lower = filename.lower()
    is_image = any([filename_lower.endswith('.%s' % extension) for extension in extensions])
    is_jpg = any([filename_lower.endswith('.%s' % jpg_extension) for jpg_extension in jpg_extensions])

    if is_jpg:
        _optimize_jpeg(filename)
    elif is_image:
        _optimize_non_jpeg_image(filename)
    else:
        pass  # skip non-images


def _optimize_jpeg(filename):
    logger.info('Optimizing « %s » with mozjpeg...' % filename)

    try:
        mozjpeg.optimize(filename)
        fix_permissions(filename)
    except Exception:
        logger.exception('An error occurred during optimization with mozjpeg')


def _optimize_non_jpeg_image(filename):
    logger.info('Optimizing « %s » with Pillow...' % filename)

    try:
        image = Image.open(filename)
        image.thumbnail((max_image_width, max_image_height), Image.ANTIALIAS)
        image.save(filename, quality=80, optimize=True)
        fix_permissions(filename)
    except Exception:
        logger.exception('An error occurred during optimization with Pillow')
