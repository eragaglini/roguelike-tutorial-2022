#!/usr/bin/env python3
# https://rogueliketutorials.com/tutorials/tcod/v2/part-0/
# https://www.reddit.com/r/roguelikedev/comments/sfwtui/2022_in_roguelikedev_libtcod_pythontcod/
# https://dev.to/adamlombard/how-to-use-the-black-python-code-formatter-in-vscode-3lo0
# https://stackoverflow.com/questions/65173291/git-push-error-src-refspec-main-does-not-match-any-on-linux
import tcod

import color
from engine import Engine
from entity import Entity
from procgen import generate_dungeon
import entity_factories
import copy

# https://stackoverflow.com/questions/38286718/what-does-def-main-none-do
def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 43

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30
    max_monsters_per_room = 2
    
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    player = copy.deepcopy(entity_factories.player)
    engine = Engine(player=player)

    engine.game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        engine=engine,
        player=player
    )
    engine.update_fov()
    
    engine.message_log.add_message(
        "Hello and welcome, adventurer, to yet another dungeon!", color.welcome_text
    )


    # https://www.geeksforgeeks.org/with-statement-in-python/
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            root_console.clear()
            engine.event_handler.on_render(console=root_console)
            context.present(root_console)

            engine.event_handler.handle_events(context)



if __name__ == "__main__":
    main()