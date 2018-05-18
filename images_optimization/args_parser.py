import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Images optimization')
    parser.add_argument('directory')
    args = parser.parse_args()

    return args
