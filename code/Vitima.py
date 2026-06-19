from code.Const import ENTITY_SPEED, ENTITY_HEALTH
from code.Entity import Entity


class Vitima(Entity):
    def __init__(self, name: str, position: tuple, ani_index: int):
        super().__init__(name, position, ani_index)
        self.ani_index = str(ani_index)
        self.entity_speed = ENTITY_SPEED[self.name]
        self.health =ENTITY_HEALTH[self.name]

    def move(self):
        self.rect.centerx -= self.entity_speed #movimento do enemies de direita a esquerda





