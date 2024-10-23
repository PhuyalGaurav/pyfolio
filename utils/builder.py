from jinja2 import Environment, FileSystemLoader
import os


def build():
    print("Building the portfolio")

    # Define paths
    config_folder = "config"
    template_folder = "src"
    template_file = "index.html"

    # Load the Jinja2 environment
    env = Environment(loader=FileSystemLoader(template_folder))
    template = env.get_template(template_file)

    # Read config files
    config_data = {}
    for i, filename in enumerate(sorted(os.listdir(config_folder)), start=1):
        file_path = os.path.join(config_folder, filename)
        if os.path.isfile(file_path):
            with open(file_path, "r") as config_file:
                config_data[f"config_{i}"] = config_file.read()

    # Render the template with the config data
    output_content = template.render(config_data)

    # Write the rendered content to the output file
    output_file = os.path.join(template_folder, "index.html")
    with open(output_file, "w") as file:
        file.write(output_content)


if __name__ == "__main__":
    build()
