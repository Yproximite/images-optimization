#!/usr/bin/env python

import argparse
import os
import subprocess

from images_optimization import mozjpeg
from images_optimization.logger import logger


def run():
    args = _parse_args()
    directory = os.path.realpath(args.directory)

    _check_working_directory(directory)
    _check_mozjpeg_binary()


def _parse_args():
    parser = argparse.ArgumentParser(description='Images optimization')
    parser.add_argument('directory')
    args = parser.parse_args()

    return args


def _check_working_directory(directory):
    if os.path.exists(directory) and os.path.isdir(directory):
        logger.info('Working directory: %s' % directory)
    elif os.path.isfile(directory):
        logger.error('Working directory is not a valid directory (%s)' % directory)
        exit(2)
    else:
        logger.error('Working directory does not exist (%s)' % directory)
        exit(2)


def _check_mozjpeg_binary():
    try:
        mozjpeg.check_binary()
        logger.info('mozjpeg binary found.')
    except subprocess.CalledProcessError as e:
        logger.error('mozjpeg binary not found.')
        exit(1)


if __name__ == '__main__':
    run()
