import pytest
from src.keyboard import Keyboard


def test_keyboard_model():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"


def test_keyboard_default_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb.language == "EN"


def test_keyboard_change_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.change_lang()
    assert kb.language == "RU"


def test_keyboard_toggle_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.change_lang()
    assert kb.language == "RU"
    kb.change_lang()
    assert kb.language == "EN"


def test_keyboard_invalid_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    with pytest.raises(ValueError):
        kb.language = 'CH'
