from enum import Enum
from typing import Tuple, List
from levelup.position import Position


class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"


class GameMap:
    starting_position: Position = Position(0, 0)
    max_x = 10
    max_y = 10

    def __init__(self):
        pass

    def get_size(self):
        return (self.max_x * self.max_y)

    def is_valid_position(self, position: Position) -> bool:
        if (position.coordinates[0] >= self.max_x):
            return False
        if (position.coordinates[0] < 0):
            return False
        if (position.coordinates[1] >= self.max_y):
            return False
        if (position.coordinates[1] < 0):
            return False
        return True

    def calculate_position(
        self, starting_position: Position, direction: Direction
    ) -> Position:
        pass
