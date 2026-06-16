from code.Const import ENTITY_SPEED
from code.Entity import Entity


class PlayerShot(Entity):
    def __init__(self, name: str, position: tuple, ani_index: int):
        super().__init__(name="",position=position,ani_index=name)
        self.health =1

    def move(self):
        self.rect.centerx += ENTITY_SPEED['TiroDejogador']
