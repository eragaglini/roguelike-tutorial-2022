from __future__ import annotations

from typing import Iterable, Optional, TYPE_CHECKING

import numpy as np  # type: ignore
from tcod.console import Console

import tile_types

if TYPE_CHECKING:
    from entity import Entity

import tile_types


class GameMap:
    def __init__(self, width: int, height: int, entities: Iterable[Entity] = ()):
        self.width, self.height = width, height
        self.entities = set(entities)

        # numpy.full(shape, fill_value, dtype=None, order='C', *, like=None)
        # Return a new array of given shape and type, filled with fill_value.
        self.tiles = np.full((width, height), fill_value=tile_types.wall, order="F")

        self.visible = np.full((width, height), fill_value=False, order="F")  # Tiles the player can currently see
        self.explored = np.full((width, height), fill_value=False, order="F")  # Tiles the player has seen before

    def get_blocking_entity_at_location(self, location_x: int, location_y: int) -> Optional[Entity]:
        for entity in self.entities:
            if entity.blocks_movement and entity.x == location_x and entity.y == location_y:
                return entity

        return None

    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside of the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        """
        Renders the map.

        If a tile is in the "visible" array, then draw it with the "light" colors.
        If it isn't, but it's in the "explored" array, then draw it with the "dark" colors.
        Otherwise, the default is "SHROUD".

        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]
        
        The first part of the statement, console.tiles_rgb[0:self.width, 0:self.height], hasn’t changed. 
        But instead of just setting it to self.tiles["dark"], we’re using np.select.

        np.select allows us to conditionally draw the tiles we want, based on what’s specified in condlist. 
        Since we’re passing [self.visible, self.explored], it will check if the tile being drawn is either visible, then explored. 
        If it’s visible, it uses the first value in choicelist, in this case, self.tiles["light"]. If it’s not visible, but explored, then we draw self.tiles["dark"]. 
        If neither is true, we use the default argument, which is just the SHROUD we defined earlier.
        """
        console.tiles_rgb[0:self.width, 0:self.height] = np.select(
            condlist=[self.visible, self.explored],
            choicelist=[self.tiles["light"], self.tiles["dark"]],
            default=tile_types.SHROUD
        )

        for entity in self.entities:
            # Only print entities that are in the FOV
            if self.visible[entity.x, entity.y]:
                console.print(x=entity.x, y=entity.y, string=entity.char, fg=entity.color)