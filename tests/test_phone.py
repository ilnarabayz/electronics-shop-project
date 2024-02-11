import pytest

from src.item import Item
from src.phone import Phone
from src.hard import Hard


def test_add_phone():
    hard = Hard("iPhone 14", 120_000, 5)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)

    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    with pytest.raises(ValueError):
        assert phone1 + hard == 10
    with pytest.raises(ValueError):
        assert item1 + hard == 25


def test_str():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)

    assert str(phone1) == 'iPhone 14'
    assert str(phone1) != "XIAOMI"


def test_repr():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)

    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim():
    phone = Phone("Samsung Galaxy", 799.99, 5, 1)

    phone.number_of_sim = 2
    assert phone.number_of_sim == 2

    with pytest.raises(ValueError):
        phone.number_of_sim = -1

    with pytest.raises(ValueError):
        phone.number_of_sim = "two"


def test_phone_initialization():
    phone = Phone("iPhone X", 999.99, 10, 2)

    assert phone.name == "iPhone X"
    assert phone.price == 999.99
    assert phone.quantity == 10
    assert phone.number_of_sim == 2