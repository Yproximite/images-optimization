#!/usr/bin/env python3.5

import os

from images_optimization.args_parser import parse_args
from images_optimization.checkers import check_working_directory, check_mozjpeg_binary
from images_optimization.optimizer import optimize_images_from_directory


def run():
    args = parse_args()
    directory = os.path.realpath(args.directory)

    check_working_directory(directory)
    check_mozjpeg_binary()
    optimize_images_from_directory(directory)


if __name__ == '__main__':
    run()
