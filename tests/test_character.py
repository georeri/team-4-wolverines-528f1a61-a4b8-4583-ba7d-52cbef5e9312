from unittest import TestCase
from levelup.character import Character, InvalidMoveException
from levelup.map import GameMap, Direction
from levelup.position import Position


class TestCharacter(TestCase):
    def test_init(self):
        expected_name = "arbitrary"
        testobj = Character(expected_name)
        self.assertEqual(testobj.name, expected_name)
        expected_position = None
        self.assertEqual(testobj.position, expected_position)

    def test_get_name(self):
        expected_name = "arbitrary"
        testobj = Character(expected_name)
        self.assertEqual(testobj.getname(), expected_name)

    def test_get_position(self):
        expected_name = "arbitrary"
        testobj = Character(expected_name)
        expected_position = None
        print(expected_position)
        self.assertEqual(testobj.getposition(), expected_position)

    def test_move_new_position(self):
        expected_name = "arbitrary"
        testobj = Character(expected_name)
        expected_position = Position(0, 1)
        testobj.position = Position(0, 0)
        testobj.map = GameMap()
        testmap = GameMap()
        testobj.enter_map(testmap)
        testobj.move(Direction.NORTH)
        self.assertEqual(testobj.position, expected_position)

    def test_enter_map(self):
        expected_name = "arbitrary"
        testobj = Character(expected_name)
        testobj.map = GameMap()
        testmap = GameMap()
        testobj.enter_map(testmap)
        numpositions = 100
        self.assertEqual(numpositions, testobj.map.get_size())

        
