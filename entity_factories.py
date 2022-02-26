from components.ai import HostileEnemy
from components.fighter import Fighter
from entity import Actor

"""
i parametri per inizializzare gli "attori", cioè il giocatore e gli npc che giocano sono:

- carattere che li rappresenta
- colore 
- nome 
- tipo di intelligenza artificiale che usano (riceve una classe come parametro)
- fighter: un'istanza della classe fighter
"""
player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    #fighter=Fighter(hp=30, defense=2, power=5),
    fighter=Fighter(hp=30, defense=2000, power=5000),
)

orc = Actor(
    char="o",
    color=(63, 127, 63),
    name="Orc",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
)
troll = Actor(
    char="T",
    color=(0, 127, 0),
    name="Troll",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, defense=1, power=4),
)