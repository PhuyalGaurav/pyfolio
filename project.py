import argparse
import os
import json
import shutil
import random
import colorsys
from jinja2 import Environment, FileSystemLoader


def parse_config_content(content):
    config_dict = {}
    lines = content.strip().split("\n")
    for line in lines:
        if "=" in line:
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip("'\"")
            if "_" in key:
                prefix, suffix = key.split("_", 1)
                if prefix not in config_dict:
                    config_dict[prefix] = []
                if suffix.isdigit():
                    entry_index = int(suffix) - 1
                    while len(config_dict[prefix]) <= entry_index:
                        config_dict[prefix].append({})
                    config_dict[prefix][entry_index][suffix] = value
                else:
                    if not config_dict[prefix]:
                        config_dict[prefix].append({})
                    config_dict[prefix][0][suffix] = value
            else:
                config_dict[key] = value
    return config_dict


def build(
    template_folder="src",
    config_folder="config",
    output_folder="output",
    template_file="index.html",
):

    # Load the Jinja2 environment
    env = Environment(loader=FileSystemLoader(template_folder))
    template = env.get_template(template_file)

    # Read config files
    config_data = {}
    for filename in sorted(os.listdir(config_folder)):
        if filename.endswith(".txt"):
            file_path = os.path.join(config_folder, filename)
            if os.path.isfile(file_path):
                with open(file_path, "r") as config_file:
                    content = config_file.read()
                    name, _ = os.path.splitext(filename)  # Remove the .txt extension
                    config_data[name] = parse_config_content(content)

    # Convert config data to JSON
    json_data = json.dumps(config_data, indent=4)

    # Render the template with the config data
    output_content = template.render(config_data=config_data, json_data=json_data)

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Copy everything from src to output
    for item in os.listdir(template_folder):
        src_path = os.path.join(template_folder, item)
        dst_path = os.path.join(output_folder, item)
        if os.path.isdir(src_path):
            shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
        else:
            shutil.copy2(src_path, dst_path)

    # Write the rendered content to the output file
    output_file = os.path.join(output_folder, "index.html")
    with open(output_file, "w") as file:
        file.write(output_content)

    print("Build completed.")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_number_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def ask_question(question, valid_answers):
    while True:
        clear_screen()
        answer = input(question + "\n")
        if valid_answers == "yn":
            if answer == "n" or answer == "N" or answer == "no" or answer == "No":
                return False
            else:
                return True
        if answer in valid_answers:
            return answer
        else:
            print(
                f"Invalid input. Please enter one of the following options: {', '.join(valid_answers)}"
            )


def navbar_questions():
    use_about = ask_question("Do you want to include an about section? (y/n)", "yn")
    use_skills = ask_question("Do you want to include a skills section? (y/n)", "yn")
    use_education = ask_question(
        "Do you want to include an education section? (y/n)", "yn"
    )
    use_experience = ask_question(
        "Do you want to include an past experiences section? (y/n)", "yn"
    )
    use_projects = ask_question(
        "Do you want to include a projects section? (y/n)", "yn"
    )
    use_contact = ask_question("Do you want to include a contact section? (y/n)", "yn")
    use_socials = ask_question("Do you want to include a socials section? (y/n)", "yn")
    return (
        use_about,
        use_skills,
        use_education,
        use_experience,
        use_projects,
        use_contact,
        use_socials,
    )


def main():
    clear_screen()
    print(
        "Welcome to pyfolio. Your portfolio generator!\nUse the number keys to select answers!"
    )
    input("Press Enter to continue...")
    theme = ask_question("Use Random theme? (y/n)", "yn")
    (
        use_about,
        use_skills,
        use_education,
        use_experience,
        use_projects,
        use_contact,
        use_socials,
    ) = navbar_questions()
    no_of_skills = get_number_input("Enter the number of skills you want to include: ")
    no_of_education = get_number_input(
        "Enter the number of education you want to include: "
    )
    no_of_experience = get_number_input(
        "Enter the number of experience you want to include: "
    )
    no_of_projects = get_number_input(
        "Enter the number of projects you want to include: "
    )
    print("Generating template...")
    return (
        theme,
        use_about,
        use_skills,
        use_education,
        use_experience,
        use_projects,
        use_contact,
        use_socials,
        no_of_skills,
        no_of_education,
        no_of_experience,
        no_of_projects,
    )


def generate_random_color():
    h = random.random()
    s = 0.5 + random.random() / 2.0
    v = 0.5 + random.random() / 2.0
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}"


def generate_random_theme():
    theme_type = random.choice(
        ["Monochromatic", "Analogous", "Complementary", "Split Complementary"]
    )
    base_color = generate_random_color()
    h, s, v = colorsys.rgb_to_hsv(
        int(base_color[1:3], 16) / 255.0,
        int(base_color[3:5], 16) / 255.0,
        int(base_color[5:7], 16) / 255.0,
    )

    if theme_type == "Monochromatic":
        colors = [colorsys.hsv_to_rgb(h, s * i, v * i) for i in [1, 0.8, 0.6, 0.4, 0.2]]
    elif theme_type == "Analogous":
        colors = [
            colorsys.hsv_to_rgb((h + i / 12.0) % 1.0, s, v) for i in [-1, 0, 1, 2, 3]
        ]
    elif theme_type == "Complementary":
        colors = [
            colorsys.hsv_to_rgb((h + i / 2.0) % 1.0, s, v) for i in [0, 0.5, 1, 1.5, 2]
        ]
    elif theme_type == "Split Complementary":
        colors = [
            colorsys.hsv_to_rgb((h + i / 3.0) % 1.0, s, v) for i in [0, 1, 2, 3, 4]
        ]

    colors = [
        f"#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}" for r, g, b in colors
    ]
    return {
        "Text": colors[0],
        "Background": colors[1],
        "Primary": colors[2],
        "Secondary": colors[3],
        "Accent": colors[4],
    }


def generator():
    (
        theme,
        use_about,
        use_skills,
        use_education,
        use_experience,
        use_projects,
        use_contact,
        use_socials,
        no_of_skills,
        no_of_education,
        no_of_experience,
        no_of_projects,
    ) = main()

    os.makedirs(os.path.dirname("config/home.txt"), exist_ok=True)
    with open("config/home.txt", "w") as file:
        file.write(
            "main_text='Add Main webpage text'\n"
            "sub_text='add subtext here'\n"
            "profile_picture='add your photo url keep it in img/'\n"
        )

    os.makedirs(os.path.dirname("config/theme.txt"), exist_ok=True)
    with open("config/theme.txt", "w") as file:
        if theme == True:
            random_theme = generate_random_theme()
            for key, value in random_theme.items():
                file.write(f"{key}={value}\n")
                print(f"{key}={value}\n")
        else:
            print("Using default theme")
            file.write(
                "Text=#050315\n"
                "Background=#fbfbfe\n"
                "Primary=#2f27ce\n"
                "Secondary=#dedcff\n"
                "Accent=#433bff\n"
            )

    if use_about:
        os.makedirs(os.path.dirname("config/about.txt"), exist_ok=True)
        with open("config/about.txt", "w") as file:
            file.write(
                "main_text='Add title for about me'\n"
                "sub_text='Add sub text for about me'\n"
            )
    if use_skills:
        os.makedirs(os.path.dirname("config/skills.txt"), exist_ok=True)
        with open("config/skills.txt", "w") as file:
            for i in range(no_of_skills):
                file.write(
                    f"Skill number {i + 1}\n"
                    f"skill{i + 1}_title='Enter title here'\n"
                    "# Enter the skill level from 1 to 100\n"
                    f"skill{i + 1}_level=50\n"
                    f"skill{i + 1}_color=#ffffff\n"
                    "# Enter the icon url use: https://fontawesome.com/icons/t-rex \n"
                    f'skill{i + 1}_icon="https://fontawesome.com/icons/t-rex?f=duotone&s=solid"\n'
                    "\n\n"
                )
    if use_education:
        os.makedirs(os.path.dirname("config/education.txt"), exist_ok=True)
        with open("config/education.txt", "w") as file:
            for i in range(no_of_education):
                file.write(
                    f"Education number {i + 1}\n"
                    f"education{i + 1}_title='Enter title here'\n"
                    f"education{i + 1}_date='Enter date'\n"
                    f"education{i + 1}_description='Enter description here'\n"
                    "\n\n"
                )

    if use_experience:
        os.makedirs(os.path.dirname("config/experience.txt"), exist_ok=True)
        with open("config/experience.txt", "w") as file:
            for i in range(no_of_experience):
                file.write(
                    f"Experience number {i + 1}\n"
                    f"experience{i + 1}_title='Enter title here'\n"
                    f"experience{i + 1}_date='Enter date'\n"
                    f"experience{i + 1}_description='Enter description here'\n"
                    "\n\n"
                )

    if use_projects:
        os.makedirs(os.path.dirname("config/projects.txt"), exist_ok=True)
        with open("config/projects.txt", "w") as file:
            for i in range(no_of_projects):
                file.write(
                    f"Project number {i + 1}\n"
                    f"project{i + 1}_title='Enter title here'\n"
                    f"project{i + 1}_date='Enter date'\n"
                    f"project{i + 1}_description='Enter description here'\n"
                    f"project{i + 1}_link='Enter link here or leave blank'\n"
                    "\n\n"
                )

    if use_contact:
        os.makedirs(os.path.dirname("config/contact.txt"), exist_ok=True)
        with open("config/contact.txt", "w") as file:
            file.write(
                "# Leave blank if you don't want to include any\n"
                "email='Example@email.com'\n"
                "phone=09989823\n"
            )

    if use_socials:
        os.makedirs(os.path.dirname("config/socials.txt"), exist_ok=True)
        with open("config/socials.txt", "w") as file:
            file.write(
                "# Leave blank if you don't want to include any\n"
                "github='https://github.com'\n"
                "linkedin='https://linkedin.com'\n"
                "twitter='https://twitter.com'\n"
                "instagram='https://instagram.com'\n"
                "facebook='https://facebook.com'\n"
                "youtube='https://youtube.com'\n"
            )
    print("Template generated successfully!")


def check_config():

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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pyfolio: Your portfolio generator")
    parser.add_argument(
        "--build", "-b", action="store_true", help="Build the portfolio"
    )
    parser.add_argument(
        "--template",
        "-t",
        action="store_true",
        help="Generate a new template for your information",
    )
    args = parser.parse_args()

    if args.build:
        build()
    elif args.template:
        check_config()
    else:
        print("Please provide an argument. Use --help for more information")
