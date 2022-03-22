import display.entity.entity as entity

import textures.bird as t_bird


class Bird(entity.Entity):
    """Cette classe permet de gérer les oiseaux"""
    def __init__(self):
        super().__init__()
        self.set_sprite_sheet(t_bird.bird_animation)
        self.y = 50

    def render(self, console, game):
        """Permet de faire le rendu de l'oiseau et de l'inclure dans l'object console
        avant l'affichage """
        console.blit(self.get_sprite(), self.x, self.y)
