import argparse
import os
from utils.generator import generator
from utils.builder import build

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Pyfolio: Your portfolio generator")
    parser.add_argument('--build', '-b', action='store_true',
                        help="Build the portfolio")
    parser.add_argument('--template', '-t', action='store_true',
                        help="Generate a new template for your information")
    args = parser.parse_args()

    if args.build:
        build()
    if args.template:
        if os.path.exists('config/home.txt'):
            a = input(
                "A previous config file was found. Do you want to overwrite it? (y/n): ")
            if a == 'y':
                generator()
            else:
                print("Exiting...")
        else:
            generator()
    else:
        print("Please provide an argument. Use --help for more information")
