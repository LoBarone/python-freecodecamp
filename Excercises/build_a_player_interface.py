import random
from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self) -> None:
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self) -> tuple:
        move = random.choice(self.moves)
        self.position = tuple(a + b for a, b in zip(move, self.position))
        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self) -> None:
        super().__init__()

        self.moves = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

    def level_up(self):
        diagonal_moves = [
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1)
        ]
        self.moves += diagonal_moves
