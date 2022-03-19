import display.entity.entity as entity

import textures.sheep as t_sheep

BLACK_SHEEP = True
WHITE_SHEEP = False

class Sheep(entity.Entity):
    def __init__(self, sheep_color, floor_height):
        super().__init__() # permet d'appeler le constructeur de la superclass
        # ici entity.Entity
        self.y = floor_height - 24

        self.__color = sheep_color
        if(self.__color == BLACK_SHEEP):
            self.set_sprite_sheet(t_sheep.black_sheep_animation)
        else:
            self.set_sprite_sheet(t_sheep.white_sheep_animation)


    def render(self, console, game):
        """Permet de faire le rendu du mouton et de l'inclure dans l'object console
        avant l'affichage """
        console.blit(self.get_sprite(), self.x, self.y)

    def get_color(self):
        """Renvoie la color du monton. Les valeurs retournées
        dépende des variables BLACK_SHEEP et WHITE_SHEEP"""
        return self.__color

    def get_pixel_positions(self):
        """Override de la méthode de la superclass pour que les colisions ne soit pas détécter sur la moitié arrière
        du mouton"""
        pixel_positions = super().get_pixel_positions()
        new_pixel_positions = []

        for pp_pos in pixel_positions:
            if(pp_pos[1] < self.x + self.width / 2):
                new_pixel_positions.append(pp_pos)
        return new_pixel_positions
