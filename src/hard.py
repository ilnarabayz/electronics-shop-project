class Hard:
    def __init__(self, name: str, price: float, quantity: int):
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __add__(self, other):
        return self.quantity + other.quantity