from __future__ import annotations

import copy
from typing import Tuple, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from game_map import GameMap

T = TypeVar("T", bound="Entity")


class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """
    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        char: str = "?",
        color: Tuple[int, int, int] = (255, 255, 255),
        name: str = "<Unnamed>",
        # blocks_movement describes whether or not this Entity can be moved over or not. 
        # Enemies will have blocks_movement set to True, while in the future, things like 
        # consumable items and equipment will be set to False.
        blocks_movement: bool = False,
    ):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks_movement = blocks_movement

    """
    The more complex section is the spawn method. It takes the GameMap instance, along with x and y for locations. 
    It then creates a clone of the instance of Entity, and assigns the x and y variables to it (this is why we don’t 
    need x and y in the initializer anymore, they’re set here). It then adds the entity to the gamemap’s entities, 
    and returns the clone.
    """
    def spawn(self: T, gamemap: GameMap, x: int, y: int) -> T:
        """Spawn a copy of this instance at the given location."""
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        gamemap.entities.add(clone)
        return clone

    def move(self, dx: int, dy: int) -> None:
        # Move the entity by a given amount
        self.x += dx
        self.y += dy