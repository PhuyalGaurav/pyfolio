> main.py & project.py does the same thing. The only difference is that the whole of project.py is in a single file.

# pyfolio

`pyfolio` is a portfolio generator written in Python. pyfolio makes it easy to generate portfolio websites in Seconds 🤯. 

## [DEMO VIDEO](https://youtu.be/Z43yPZwkWDo) (For CS50p)

## Features

- Generate a portfolio with sections for about, skills, education, experience, projects, contact, and socials.
- Customize the number of entries for skills, education, experience, and projects.
- Option to use a random theme or specify your own theme colors.
- Automatically generates configuration files based on user input.
## Project Tree

## Requirements

- Python 3.x
- pip
- git

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/pyfolio.git
    cd pyfolio
    ```

2. Install the required dependencies (if any).
   
   ```sh
   # Initialize a venv (optional)
   python -m venv venv
   # In windows
   venv/Script/activate.bat
   # In MacOs / Linux (POSIX)
   source venv/bin/activate

   # Install the requirements
   pip install -r requirements.txt
   ```

## Usage
### 1. Run the `main.py` file with one of the following options:

```sh
python main.py --template
```
or 
```sh
python main.py -t
```

This will generate a new template for your information. If a previous config file is found, you will be prompted to overwrite it.


### 2. Answer the questions asked.

    # Example response

    Welcome to pyfolio. Your portfolio generator!
    Use the number keys to select answers!
    Press Enter to continue...
    Use Random theme? (y/n): y
    Do you want to include an about section? (y/n): y
    Do you want to include a skills section? (y/n): y
    Do you want to include an education section? (y/n): y
    Do you want to include a past experiences section? (y/n): y
    Do you want to include a projects section? (y/n): y
    Do you want to include a contact section? (y/n): y
    Do you want to include a socials section? (y/n): y
    Enter the number of skills you want to include: 3
    Enter the number of education you want to include: 2
    Enter the number of experience you want to include: 2
    Enter the number of projects you want to include: 3
    Generating template...
### 3. Configure the files in the config folder. See [Configuration](#configuration) for Guidance.

### 4. Build 
After the configuration is done build the website using :
```sh
python main.py --build
```
or

```sh
python main.py -b
```
Your portfolio will be built in /output folder.

## Configuration

The configuration files are generated based on your input and saved in the `config` folder. You can manually edit these files to further customize your portfolio.

### Example Configuration Files

- `home.txt`:

    ```plaintext
    main_text='Add Main webpage text'
    sub_text='add subtext here'
    profile_picture='add your photo url keep it in img/'
    ```

- `theme.txt`:

    ```plaintext
    Text=#050315
    Background=#fbfbfe
    Primary=#2f27ce
    Secondary=#dedcff
    Accent=#433bff
    ```

- `about.txt`:

    ```plaintext
    main_text='Add title for about me'
    sub_text='Add sub text for about me'
    ```

- `skills.txt`:

    ```plaintext
    Skill number 1
    skill1_title='Enter title here'
    skill1_level=50
    skill1_color=#ffffff
    skill1_icon="https://fontawesome.com/icons/t-rex?f=duotone&s=solid"
    ```

- `education.txt`:

    ```plaintext
    Education number 1
    education1_title='Enter title here'
    education1_date='Enter date'
    education1_description='Enter description here'
    ```

- `experience.txt`:

    ```plaintext
    Experience number 1
    experience1_title='Enter title here'
    experience1_date='Enter date'
    experience1_description='Enter description here'
    ```

- `projects.txt`:

    ```plaintext
    Project number 1
    project1_title='Enter title here'
    project1_date='Enter date'
    project1_description='Enter description here'
    project1_link='Enter link here or leave blank'
    ```

- `contact.txt`:

    ```plaintext
    email='Example@email.com'
    phone=09989823
    ```

- `socials.txt`:

    ```plaintext
    github='https://github.com'
    linkedin='https://linkedin.com'
    twitter='https://twitter.com'
    instagram='https://instagram.com'
    facebook='https://facebook.com'
    youtube='https://youtube.com'
    ```
    ! IMPORTANT Keep the images used in the /img folder.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
