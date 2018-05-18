#!/usr/bin/env python

import os

from images_optimization.args_parser import parse_args
from images_optimization.checkers import check_working_directory, check_mozjpeg_binary


def run():
    args = parse_args()
    directory = os.path.realpath(args.directory)

    check_working_directory(directory)
    check_mozjpeg_binary()


if __name__ == '__main__':
    run()
