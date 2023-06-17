from abc import abstractmethod, ABCMeta


class Player(metaclass=ABCMeta):
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    @abstractmethod
    def choose_column(self):
        pass
