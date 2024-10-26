import argparse
import os
from utils.builder import build
from utils.generator import generator
from utils.colors import generate_random_theme


def regenerate_theme():
    os.makedirs(os.path.dirname("config/theme.txt"), exist_ok=True)
    with open("config/theme.txt", "w") as file:
        random_theme = generate_random_theme()
        for key, value in random_theme.items():
            file.write(f"{key}={value}\n")


def main():
    parser = argparse.ArgumentParser(description="Portfolio Builder")
    parser.add_argument("--build", action="store_true", help="Build the portfolio")
    parser.add_argument(
        "--template", action="store_true", help="Generate a new template"
    )
    parser.add_argument(
        "--regenerate-theme",
        action="store_true",
        help="Regenerate the theme and build the portfolio",
    )
    args = parser.parse_args()

    if args.build:
        build()
    elif args.template:
        if os.path.exists("config/home.txt"):
            a = input(
                "A previous config file was found. Do you want to overwrite it? (y/n): "
            )
            if a == "y":
                generator()
            else:
                print("Exiting...")
        else:
            generator()
    elif args.regenerate_theme:
        regenerate_theme()
        build()
    else:
        print("Please provide an argument. Use --help for more information")


if __name__ == "__main__":
    main()
