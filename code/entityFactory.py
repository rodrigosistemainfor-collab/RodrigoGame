#!/usr/bin/python
# -*- coding: utf-8 -*-
from Const import WIN_WIDTH
from code.background import Background


class EntityFactory:

    @classmethod
    def get_entity(cls, entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(name=f'Level1Bg{i}', position=(0, 0)))
                    list_bg.append(Background(name=f'Level1Bg{i}', position=(WIN_WIDTH, 0)))
                return list_bg
