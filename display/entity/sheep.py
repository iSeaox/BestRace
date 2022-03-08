import display.entity.entity as entity

import textures.sheep as t_sheep

BLACK_SHEEP = True
WHITE_SHEEP = False

class Sheep(entity.Entity):
    def __init__(self, sheep_color):
        super().__init__()
        self.__color = sheep_color
        if(self.__color == BLACK_SHEEP):
            self.__sprite_sheet = t_sheep.black_sheep
        else:
            self.__sprite_sheet = t_sheep.white_sheep


    def render(self, console, floor_height):
        console.blit(self.get_sprite(self.tick), self.x, self.y)

    def get_color(self):
        return self.__color
