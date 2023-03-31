from unittest import TestCase
from unittest.mock import MagicMock, create_autospec
from levelup.controller import GameController, CharacterNotFoundException
from levelup.character import DEFAULT_CHARACTER_NAME, InvalidMoveException, Character
from levelup.map import Direction
from levelup.position import Position


class TestGameController(TestCase):
    def test_init(self):
        testobj = GameController()
        self.assertEqual(testobj.status.move_count, 0)
        self.assertEqual(
            testobj.status.current_position,
            Position(11,11),
        )

    def test_set_character_position(self): 
        testobj = GameController()
        testobj.status.set_character_position(Position(11,11))
        self.assertEqual(testobj.status.current_position, Position(11,11))

    def test_move(self):
         testobj = GameController()
         testobj.create_character("Eric")
         testobj.start_game()
         cp = testobj.character.getposition()
         testobj.character.move("n")
         self.assertNotEqual(testobj.character.getposition(), cp)

    def test_set_character_position(self):
        self.assertEqual(1, 2)

    def test_get_total_positions(self):
        testobj = GameController()
        self.assertEqual(testobj.map.get_total_positions(),100)
    

    def test_create_character(self):
        self.assertEqual(1, 2)

    def test_start_game(self):
        self.assertEqual(1, 2)
