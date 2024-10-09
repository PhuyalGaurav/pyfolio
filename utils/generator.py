import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def ask_question(question, valid_answers):
    while True:
        clear_screen()
        answer = input(question + "\n")
        if valid_answers == 'yn':
            if answer == 'n' or answer == "N" or answer == "no" or answer == "No":
                return False
            else:
                return True
        if answer in valid_answers:
            return answer
        else:
            print(
                f"Invalid input. Please enter one of the following options: {', '.join(valid_answers)}")


def navbar_questions():
    use_about = ask_question(
        "Do you want to include an about section? (y/n)", 'yn'
    )
    use_skills = ask_question(
        "Do you want to include a skills section? (y/n)", 'yn'
    )
    use_education = ask_question(
        "Do you want to include an education section? (y/n)", 'yn'
    )
    use_experience = ask_question(
        "Do you want to include an past experiences section? (y/n)", 'yn'
    )
    use_projects = ask_question(
        "Do you want to include a projects section? (y/n)", 'yn'
    )
    use_contact = ask_question(
        "Do you want to include a contact section? (y/n)", 'yn'
    )
    use_socials = ask_question(
        "Do you want to include a socials section? (y/n)", 'yn'
    )
    return use_about, use_skills, use_education, use_experience, use_projects, use_contact, use_socials


def main():
    clear_screen()
    print("Welcome to pyfolio. Your portfolio generator!\nUse the number keys to select answers!")
    input("Press Enter to continue...")
    theme = ask_question(
        "Use Random theme? (y/n)", 'yn'
    )
    use_about, use_skills, use_education, use_experience, use_projects, use_contact, use_socials = navbar_questions()
    no_of_skills = int(
        input("Enter the number of skills you want to include: "))
    no_of_education = int(
        input("Enter the number of education you want to include: "))
    no_of_experience = int(
        input("Enter the number of experience you want to include: "))
    no_of_projects = int(
        input("Enter the number of projects you want to include: "))
    print("Generating template...")
    return theme, use_about, use_skills, use_education, use_experience, use_projects, use_contact, use_socials, no_of_skills, no_of_education, no_of_experience, no_of_projects


def generator():
    theme, use_about, use_skills, use_education, use_experience, use_projects, use_contact, use_socials, no_of_skills, no_of_education, no_of_experience, no_of_projects = main()

    os.makedirs(os.path.dirname("config/home.txt"), exist_ok=True)
    with open("config/home.txt", 'w') as file:
        file.write(
            "main_text=\n"
            "sub_text=\n"
            "profile_picture=\n"
        )

    os.makedirs(os.path.dirname("config/theme.txt"), exist_ok=True)
    with open("config/theme.txt", 'w') as file:
        if theme == 'y':
            file.write("random=True")
        else:
            file.write(
                "Text=#050315\n"
                "Background=#fbfbfe\n"
                "Primary=#2f27ce\n"
                "Secondary=#dedcff\n"
                "Accent=#433bff\n"
            )

    if use_about:
        os.makedirs(os.path.dirname("config/about.txt"), exist_ok=True)
        with open("config/about.txt", 'w') as file:
            file.write(
                "main_text='Add title for about me'\n"
                "sub_text='Add sub text for about me'\n"
            )
    if use_skills:
        os.makedirs(os.path.dirname("config/skills.txt"), exist_ok=True)
        with open("config/skills.txt", 'w') as file:
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
        with open("config/education.txt", 'w') as file:
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
        with open("config/experience.txt", 'w') as file:
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
        with open("config/projects.txt", 'w') as file:
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
        with open("config/contact.txt", 'w') as file:
            file.write(
                "# Leave blank if you don't want to include any\n"
                "email='Example@email.com'\n"
                "phone=09989823\n"
            )

    if use_socials:
        os.makedirs(os.path.dirname("config/socials.txt"), exist_ok=True)
        with open("config/socials.txt", 'w') as file:
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
