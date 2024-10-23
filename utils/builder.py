import os
import json
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
                entry_index = (
                    int("".join(filter(str.isdigit, suffix))) - 1
                    if suffix.isdigit()
                    else 0
                )
                while len(config_dict[prefix]) <= entry_index:
                    config_dict[prefix].append({})
                config_dict[prefix][entry_index][suffix] = value
            else:
                config_dict[key] = value
    return config_dict


def build():
    config_folder = "config"
    template_folder = "src"
    template_file = "index.html"

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
    print(json_data)

    # Write the rendered content to the output file
    output_file = os.path.join(template_folder, "index.html")
    with open(output_file, "w") as file:
        file.write(output_content)


if __name__ == "__main__":
    build()
