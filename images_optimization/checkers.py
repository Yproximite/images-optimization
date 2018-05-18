import os
import subprocess

from images_optimization import mozjpeg
from images_optimization.logger import logger


def check_working_directory(directory):
    if os.path.exists(directory) and os.path.isdir(directory):
        logger.info('Working directory: %s' % directory)
    elif os.path.isfile(directory):
        logger.error('Working directory is not a valid directory (%s)' % directory)
        exit(2)
    else:
        logger.error('Working directory does not exist (%s)' % directory)
        exit(2)


def check_mozjpeg_binary():
    try:
        mozjpeg.check_binary()
        logger.info('mozjpeg binary found.')
    except subprocess.CalledProcessError as e:
        logger.error('mozjpeg binary not found.')
        exit(1)
