from levelup.controller import GameController
from levelup.controller import Direction
from levelup.position import Position
from levelup.map import Direction, GameMap


class MoveLibrary:
    start_x: int
    start_y: int
    move_count: int

    def initialize_character_xposition_with(self, x_position):
        self.start_x = x_position 

    def initialize_character_yposition_with(self, y_position):
        self.start_y = y_position

    def initialize_character_moveCount_with(self, move_count):
        self.move_count = move_count

    def move_in_direction(self, direction):
        self.controller = GameController()
        self.controller.create_character("Eric")
        self.controller.start_game()
        self.controller.character.setposition(Position(int(self.start_x),int(self.start_y)))
        self.controller.move(Direction[direction])

    def character_xposition_should_be(self, expected):
    
        end_x = self.controller.status.current_position.coordinates[0]
        if int(end_x) != int(expected):
            raise AssertionError(int(end_x), int(expected))
            

    def character_yposition_should_be(self, expected):
        end_y = self.controller.status.current_position.coordinates[1]
        if int(end_y) != int(expected):
            raise AssertionError(int(end_y), int(expected))
           

    def character_moveCount_should_be(self, expected):
        self.move_count = int(self.controller.status.move_count) + int(self.move_count)
        if int(self.move_count) != int(expected):
         raise AssertionError(int(self.move_count), int(expected))
