import display.entity.entity as entity

import textures.bird as t_bird

class Bird(entity.Entity):
    def __init__(self):
        super().__init__()
        self.set_sprite_sheet(t_bird.bird_animation)

    def render(self, console, game):
        console.blit(self.get_sprite(), self.x, self.y)
