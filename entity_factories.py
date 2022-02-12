from entity import Entity

# in questo file definiamo delle entità inizializzando la classe entity
# queste entità verrano poi "spawnate" mediante la funzione spawn sempre
# della stessa classe entity

player = Entity(char="@", color=(255, 255, 255), name="Player", blocks_movement=True)

orc = Entity(char="o", color=(63, 127, 63), name="Orc", blocks_movement=True)
troll = Entity(char="T", color=(0, 127, 0), name="Troll", blocks_movement=True)