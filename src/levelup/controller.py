import logging
from dataclasses import dataclass
from levelup.character import Character, DEFAULT_CHARACTER_NAME, InvalidMoveException
from levelup.map import Direction, GameMap
from levelup.position import Position

ARBITRARY_INVALID_INITIALIZED_POSITION = Position(11, 11)
@dataclass
class GameStatus:
    move_count: int = 0
    character: Character = Character(DEFAULT_CHARACTER_NAME)
    running: bool = False
    starting_position: Position = None
    
    current_position: tuple = ARBITRARY_INVALID_INITIALIZED_POSITION

    def __str__(self):
        return f"Moved {self.move_count} times, currently on position {self.current_position}, started  on position {self.starting_position}"

    def set_character_position(self, position: Position) -> None:
        print(f"Set character position state for testing")
        self.character.position = position

class CharacterNotFoundException(Exception):
    pass


class GameController:
    status: GameStatus
    character: Character

    def __init__(self):
        self.status = GameStatus()
        self.character = None
        self.map = GameMap()
        self.status.starting_position = self.map.starting_position

    def start_game(self):
        if hasattr(self, "character"):
            self.character.enter_map(self.map)
            self.status.current_position = self.character.position
            self.set_character_position(self.map.starting_position)
        else:
            raise CharacterNotFoundException("Character not found")

    def create_character(self, character_name: str) -> None:
        self.character = Character(character_name)

    def move(self, direction: Direction) -> None:
        self.character.move(direction)
        self.status.current_position=self.character.position
        self.status.move_count = self.status.move_count + 1

    def set_character_position(self, position: Position):
        self.character.position = position

    def get_total_positions(self):
        return self.map.position_count
    
    
        
