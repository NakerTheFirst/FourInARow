from abc import abstractmethod, ABC


class Player(ABC):
    def __init__(self, name, symbol):
        self._name = name
        self._symbol = symbol

    @abstractmethod
    def choose_column(self, board):
        pass

    @property
    def name(self):
        return self._name

    @property
    def symbol(self):
        return self._symbol
