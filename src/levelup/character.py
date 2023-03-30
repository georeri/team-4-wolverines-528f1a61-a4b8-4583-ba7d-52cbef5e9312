from levelup.position import Position
from levelup.map import GameMap, Direction

DEFAULT_CHARACTER_NAME = "Character"


class InvalidMoveException(Exception):
    pass


class Character:
    name: str
    map: GameMap
    position: Position = None

    def __init__(self, name: str ):
        self.name = name or DEFAULT_CHARACTER_NAME
     

    def setposition(self, position: Position ):
        self.position = position or None

    def getname(self):
        return f"{self.name}"

    def enter_map(self, game_map: GameMap):
        self.map = game_map
    

    def move(self, direction: Direction):
        currentposition = self.position

    

        match direction:
            case Direction.NORTH:
                tempposition = Position(currentposition.coordinates[0], currentposition.coordinates[1] + 1)

            case Direction.SOUTH:
                tempposition = Position(currentposition.coordinates[0], currentposition.coordinates[1] - 1)

            case Direction.EAST:
                tempposition = Position(currentposition.coordinates[0] + 1, currentposition.coordinates[1])

            case Direction.WEST:
                tempposition = Position(currentposition.coordinates[0] -1 , currentposition.coordinates[1])

            case _:
                print("Invalid direction")

        if (self.map.is_valid_position(tempposition)):
            self.position = tempposition


    def getposition(self):
        return (self.position)
