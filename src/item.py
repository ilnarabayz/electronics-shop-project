#import csv
#import os


class InstantiateCSVError(Exception):
    def __init__(self):
        self.error = 'Файл item.csv поврежден'

    def __str__(self):
        return self.error


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

        Item.all.append(self)

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
    def instantiate_from_csv(cls, path):
        """
        Создает экземпляры класса Item из данных, полученных из файла items.csv.
        """
        import csv
        import os
        cls.all.clear()
        paths = os.path.exists(path)
        if paths == False:
            raise FileNotFoundError('Отсутствует файл item.csv')
        else:
            with open(path, 'r', newline='') as attributes:
                attribute = csv.DictReader(attributes)
                for attr in attribute:
                    if 'name' not in attr:
                        raise InstantiateCSVError
                    name = attr['name']
                    if 'price' not in attr:
                        raise InstantiateCSVError
                    price = cls.string_to_number(attr['price'])
                    if 'quantity' not in attr:
                        raise InstantiateCSVError
                    quantity = cls.string_to_number(attr['quantity'])
                    items_csv = Item(name, price, quantity)
            return items_csv

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

    def __add__(self, other):
        """ Магический метод add делает проверку что:
        Экземпляр self относиться к классу self
        Экземпляр other наследуется от класса self """
        if isinstance(self, self.__class__):
            if issubclass(other.__class__, self.__class__):
                return self.quantity + other.quantity
