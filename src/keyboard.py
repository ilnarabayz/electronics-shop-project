from src import item


class LanguageMixin:
    """
    Класс Mixin для управления языковой раскладкой клавиатуры и ее изменения.
    """
    LANGUAGES = ['EN', 'RU']

    def __init__(self):

        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        """
        Дает возможность изменять язык между 'RU, EN'
        """
        if value in self.LANGUAGES:
            self.__language = value
        else:
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")

    def change_lang(self):
        """
        Переключает язык раскладки клавиатуры между доступными языками.
        """
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'


class Keyboard(item.Item, LanguageMixin):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)

    def __str__(self):
        return self.name
