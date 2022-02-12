from typing import Tuple

import numpy as np  # type: ignore

# Tile graphics structured type compatible with Console.tiles_rgb.
# dtype creates a data type which Numpy can use, which behaves similarly to a struct in a language like C. Our data type is made up of three parts:
# ch: The character, represented in integer format. We’ll translate it from the integer into Unicode. (mettiamo uno spazio vuoto perché non deve avere nessun carattere)
# fg: The foreground color. “3B” means 3 unsigned bytes, which can be used for RGB color codes.
# bg: The background color. Similar to fg.
graphic_dt = np.dtype(
    [
        ("ch", np.int32),  # Unicode codepoint.
        ("fg", "3B"),  # 3 unsigned bytes, for RGB colors.
        ("bg", "3B"),
    ]
)

# tipo "tessera", ogni rettangolo che compone la mappa, può essere camminabile, trasparente e ha un 
# tipo "grafica" all'interno, che permette di definirne il colore
# Tile struct used for statically defined tile data.
# FOV = field of view
tile_dt = np.dtype(
    [
        ("walkable", np.bool),  # True if this tile can be walked over.
        ("transparent", np.bool),  # True if this tile doesn't block FOV.
        ("dark", graphic_dt),
        ("light", graphic_dt),  # Graphics for when the tile is in FOV.  # Graphics for when this tile is not in FOV.
    ]
)

# permette di creare un nuovo tipo di tessera nella mappa, passando tre parametri:
# 1. se è possibile camminarci sopra, 2. se è trasparente, 3. la grafica
def new_tile(
    *,  # Enforce the use of keywords, so that parameter order doesn't matter.
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
    light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """Helper function for defining individual tile types """
    # numpy.array(object, dtype=None, *, copy=True, order='K', subok=False, ndmin=0, like=None)
    # Create an array.
    # dtype: The desired data-type for the array. If not given, then the type will be determined as the minimum type required to hold the objects in the sequence.
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)

# SHROUD represents unexplored, unseen tiles
SHROUD = np.array((ord(" "), (255, 255, 255), (0, 0, 0)), dtype=graphic_dt)

floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(" "), (255, 255, 255), (50, 50, 150)),
    light=(ord(" "), (255, 255, 255), (200, 180, 50)),
)
wall = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord(" "), (255, 255, 255), (0, 0, 100)),
    light=(ord(" "), (255, 255, 255), (130, 110, 50)),
)