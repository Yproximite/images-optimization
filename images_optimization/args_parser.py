import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Images optimization')
    parser.add_argument('directory')
    parser.add_argument('--after', help="Only files after specified file will be optimized ")
    args = parser.parse_args()

    return args
