import display.entity.entity as entity

import textures.sheep as t_sheep

BLACK_SHEEP = True
WHITE_SHEEP = False

class Sheep(entity.Entity):
    def __init__(self, sheep_color):
        super().__init__()
        self.__color = sheep_color
        if(self.__color == BLACK_SHEEP):
            self.set_sprite_sheet(t_sheep.black_sheep_animation)
        else:
            self.set_sprite_sheet(t_sheep.white_sheep_animation)


    def render(self, console, game):
        console.blit(self.get_sprite(), self.x, game.floor_height - 24)

    def get_color(self):
        return self.__color
