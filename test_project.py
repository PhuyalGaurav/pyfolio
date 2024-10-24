import pytest
import os
import json
from project import (
    parse_config_content,
    build,
    clear_screen,
    get_number_input,
    ask_question,
    navbar_questions,
    main,
    generator,
    check_config,
)


def test_parse_config_content():
    content = """
    key1=value1
    key2=value2
    """
    expected_output = {
        "key1": "value1",
        "key2": "value2",
    }
    assert parse_config_content(content) == expected_output


def test_clear_screen(monkeypatch):
    def mock_system(command):
        assert command in ["cls", "clear"]

    monkeypatch.setattr(os, "system", mock_system)
    clear_screen()


def test_get_number_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "5")
    assert get_number_input("Enter a number: ") == 5


def test_ask_question(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "y")
    assert ask_question("Continue? (y/n)", "yn") == True

    monkeypatch.setattr("builtins.input", lambda _: "n")
    assert ask_question("Continue? (y/n)", "yn") == False


def test_navbar_questions(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "y")
    assert navbar_questions() == (True, True, True, True, True, True, True)


def test_main(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "y")
    monkeypatch.setattr(
        "project.navbar_questions", lambda: (True, True, True, True, True, True, True)
    )
    monkeypatch.setattr("project.get_number_input", lambda _: 5)
    assert main() == (True, True, True, True, True, True, True, True, 5, 5, 5, 5)


def test_check_config(monkeypatch, tmpdir):
    config_folder = tmpdir.mkdir("config")
    config_file = config_folder.join("home.txt")
    config_file.write("key=value")

    monkeypatch.setattr("os.path.exists", lambda path: True)
    monkeypatch.setattr("builtins.input", lambda _: "y")
    monkeypatch.setattr("project.generator", lambda: None)
    check_config()
