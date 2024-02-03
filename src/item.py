import csv

import os


# noinspection PyTypeChecker
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    items = all

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        # self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[0:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls, data_file):
        """
        Создает экземпляры класса Item из данных, полученных из файла items.csv.
        """
        file_path = os.path.join(os.path.dirname(__file__), data_file)

        cls.all.clear()
        with open(file_path, 'r', newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                price = cls.string_to_number(row['price'])
                quantity = cls.string_to_number(row['quantity'])
                items_csv = Item(name, price, quantity)
                items = cls.all.append(items_csv)

            return cls.all

    @staticmethod
    def string_to_number(string):
        """
        Преобразует строку в число, если это возможно.

        :param string: Входная строка.
        :return: Число или исходная строка, если преобразование невозможно.
        """

        if string.isdigit:
            if '.' in string:
                string = int(float(string))
            else:
                string = int(string)
            return string

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name
