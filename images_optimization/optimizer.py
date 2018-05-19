import glob

from images_optimization.optimizers import mozjpeg, pillow
from images_optimization.logger import logger
from images_optimization.args_parser import parse_args
from images_optimization.permissions_fixer import fix_permissions

jpg_extensions = ['jpg', 'jpeg']
extensions = jpg_extensions + ['png', 'gif']


def optimize_images_from_directory(directory):
    handled_images = 0
    handled_images_success = 0
    handled_images_errors = 0

    filenames = _list_filenames(directory)
    filenames_len = len(filenames)

    for filename in filenames:
        handled_images += 1

        try:
            _optimize_image(filename)
            handled_images_success += 1
        except Exception:
            logger.exception('An error occurred during optimization')
            handled_images_errors += 1

        logger.info('Handled %d images on %d, with %d success and %d fails' % (
            handled_images,
            filenames_len,
            handled_images_success,
            handled_images_errors
        ))


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

    mozjpeg.optimize(filename)
    fix_permissions(filename)


def _optimize_non_jpeg_image(filename):
    logger.info('Optimizing « %s » with Pillow...' % filename)

    pillow.optimize(filename)
    fix_permissions(filename)
