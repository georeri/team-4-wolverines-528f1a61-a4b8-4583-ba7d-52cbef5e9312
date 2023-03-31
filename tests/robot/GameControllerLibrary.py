from levelup.controller import GameController


class GameControllerLibrary:

    start_x: int
    start_y: int
    move_count: int

    def initialize_character_xposition_with(self, x_position):
        self.start_x = x_position 

    def initialize_character_yposition_with(self, y_position):
        self.start_y = y_position

    def initialize_character_moveCount_with(self, move_count):
        self.move_count = move_count
    def initialize_controller(self):
        pass

    def create_character_with_name(self, charactername):
        pass

    def character_name_should_be(self, expected):
        pass

    def number_of_map_positions_should_be(self, expected):
        self.controller = GameController()
        self.controller.create_character("Eric")
        self.controller.start_game()
        if self.controller.map.get_size() != int(expected):
            raise AssertionError(int(self.controller.map.get_size()), int(expected))

    def starting_X_coordinate_should_be(self, expected):
        if int(self.controller.character.getposition().coordinates[0]) != int(expected):
            raise AssertionError(int(self.controller.character.getposition().coordinates[0]), int(expected))

    def starting_Y_coordinate_should_be(self, expected):
        if int(self.controller.character.getposition().coordinates[1]) != int(expected):
            raise AssertionError(int(self.controller.character.getposition().coordinates[1]), int(expected))

    def starting_move_count_should_be(self, expected):
         if int(self.controller.status.move_count) != int(expected):
            raise AssertionError(int(self.controller.status.move_count), int(expected))
