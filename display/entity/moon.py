import display.entity.entity as entity

import textures.ui.background as t_background


class Moon(entity.Entity):
    def __init__(self):
        super().__init__()
        self.set_sprite_sheet(t_background.moon)
        self.y = 12

    def render(self, console, game):
        console.blit(self.get_sprite(), self.x, self.y)

    def do_tick(self):
        if self.x <= -288:
            self.x = 288
        self.x -= 1
