from unittest import TestCase
from levelup.map import GameMap
from levelup.position import Position


class TestMap(TestCase):
    def test_init(self):
        testobj = GameMap()
        expected_starting_position = Position(0,0)
        self.assertEqual(testobj.starting_position, expected_starting_position)

    def test_get_size(self):
        testobj = GameMap()
        expected_size = 100
        self.assertEqual(testobj.get_size(), expected_size)

    def test_is_invalid_position(self):
        testobj = GameMap()
        expected_position = Position(11,11)
        isinvalidposition = testobj.is_valid_position(expected_position)
        self.assertEqual(isinvalidposition, False)

    def test_is_valid_position(self):
        testobj = GameMap()
        expected_position = Position(8,8)
        isvalidposition = testobj.is_valid_position(expected_position)
        self.assertEqual(isvalidposition, True)

    # Things I want to test within my GameMap class:
    # starting position
    # position validation
    # new position calculation
