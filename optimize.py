#!/usr/bin/env python

import logging
import subprocess

import coloredlogs

from images_optimization import mozjpeg

coloredlogs.install()


def run():
    _check_mozjpeg_binary()


def _check_mozjpeg_binary():
    try:
        mozjpeg.check_binary()
        logging.info('mozjpeg binary found.')
    except subprocess.CalledProcessError as e:
        logging.error('mozjpeg binary not found.')
        exit(1)


if __name__ == '__main__':
    run()
