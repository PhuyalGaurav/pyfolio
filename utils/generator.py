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
        "Do you want to include an experience section? (y/n)", 'yn'
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
    os.makedirs(os.path.dirname("config/theme.txt"), exist_ok=True)
    with open("config/theme.txt", 'w') as file:
        if theme == 'y':
            file.write("random=True")
        else:
            file.write(
                "Text=#050315\nBackground=#fbfbfe\nPrimary=#2f27ce\nSecondary=#dedcff\nAccent=#433bff\n")
    print("Template generated successfully!")
