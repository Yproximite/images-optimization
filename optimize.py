#!/usr/bin/env python

import subprocess

from images_optimization import mozjpeg
from images_optimization.logger import logger


def run():
    _check_mozjpeg_binary()


def _check_mozjpeg_binary():
    try:
        mozjpeg.check_binary()
        logger.info('mozjpeg binary found.')
    except subprocess.CalledProcessError as e:
        logger.error('mozjpeg binary not found.')
        exit(1)


if __name__ == '__main__':
    run()
