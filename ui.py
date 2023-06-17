from abc import abstractmethod, ABC


class UI(ABC):
    def __init__(self, board):
        self.board = board

    @abstractmethod
    def display(self):
        pass
