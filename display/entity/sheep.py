import display.entity.entity as entity

import textures.sheep as t_sheep

BLACK_SHEEP = True
WHITE_SHEEP = False

class Sheep(entity.Entity):
    def __init__(self, sheep_color):
        super().__init__() # permet d'appeler le constructeur de la superclass 
        # ici entity.Entity

        self.__color = sheep_color
        if(self.__color == BLACK_SHEEP):
            self.set_sprite_sheet(t_sheep.black_sheep_animation)
        else:
            self.set_sprite_sheet(t_sheep.white_sheep_animation)


    def render(self, console, game):
        """Permet de faire le rendu du mouton et de l'inclure dans l'object console
        avant l'affichage """
        console.blit(self.get_sprite(), self.x, game.floor_height - 24)

    def get_color(self):
        """Renvoie la color du monton. Les valeurs retournées
        dépende des variables BLACK_SHEEP et WHITE_SHEEP"""
        return self.__color
