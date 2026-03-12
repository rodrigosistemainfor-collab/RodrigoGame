import ent as ent

from code.Const import WIN_WIDTH
from code.EnemyShot import EnemyShot
from code.PlayerShot import PlayerShot
from code.enemy import Enemy
from code.entity import Entity


class EntityMediator:
    @classmethod
    def __verify_collision_window(cls, ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0

    @classmethod
    def verify_collision(cls, entity_list: list[Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

    @classmethod
    def verify_health(cls, entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)
