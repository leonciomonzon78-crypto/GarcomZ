from code.Const import ENTITY_SPEED
from code.Entity import Entity


class PlayerShot(Entity):
    def __init__(self, name: str, position: tuple, ani_index: int):
        super().__init__(name=name,position=position,ani_index=ani_index)
        self.health =1

    def move(self):
        self.rect.centerx += ENTITY_SPEED[self.name]
