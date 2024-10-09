import keyboard


def wait_for_key_input():
    pressed_key = None

    def on_key(event):
        nonlocal pressed_key
        pressed_key = event.name
        keyboard.unhook_all()  # Stop listening for key presses

    # Register the key event handlers for all characters
    for char in '0123456789abcdefghijklmnopqrstuvwxyz':
        keyboard.on_press_key(char, on_key)

    # Wait until a key is pressed
    while pressed_key is None:
        pass

    return pressed_key


def ask_question(question, valid_answers):
    while True:
        print(question)
        answer = wait_for_key_input()
        if answer in valid_answers:
            return answer
        else:
            print(
                f"Invalid input. Please press one of the following options: {', '.join(valid_answers)}")


def main():
    print("Welcome to pyfolio. Your portfolio generator!\nUse the number keys to select answers!")
    theme = ask_question(
        "Use Random theme (1) or Custom theme (2)?", ['1', '2'])
    print(f"Theme option selected: {theme}")


if __name__ == "__main__":
    main()
