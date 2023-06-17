from abc import abstractmethod, ABC


class Player(ABC):
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    @abstractmethod
    def choose_column(self, board):
        pass
