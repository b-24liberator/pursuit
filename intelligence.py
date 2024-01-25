# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,too-few-public-methods,invalid-name
from random import randint, randrange

from components import Position, Velocity
import entities.bullet

class Wander:
    def think(self, pos: Position, vel: Velocity):
        vel.x = randint(-1, 1)
        vel.y = randint(-1, 1)

        fire_bullet = randrange(0, 100)
        if fire_bullet <= 25:
            shellDirection = randint(1,4)
            if shellDirection == 1:
                shellDirection = 'UP'
            elif shellDirection == 2:
                shellDirection = 'DOWN'
            elif shellDirection == 3:
                shellDirection = 'LEFT'
            elif shellDirection == 4:
                shellDirection = 'RIGHT'
            entities.bullet.create(shellDirection, pos.x, pos.y)
