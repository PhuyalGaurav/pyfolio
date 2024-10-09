import argparse
from utils.generator import generator
from utils.builder import build

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Pyfolio: Your portfolio generator")
    parser.add_argument('--build', action='store_true',
                        help="Build the portfolio")
    args = parser.parse_args()

    if args.build:
        build()
    else:
        generator()
