import display.entity.entity as entity

import textures.player as t_player

class Player(entity.Entity):

    def __init__(self):
        super().__init__()
        self.is_jumping = False
        self.set_sprite_sheet(t_player.player_animation)

    def do_tick(self):
        if(self.is_jumping and self.tick == len(self.get_sprite_sheet()) - 1):
            self.is_jumping = False
            self.y -= 10
            self.set_sprite_sheet(t_player.player_animation)
        self.tick += 1
        self.tick %= len(self.get_sprite_sheet())

    def jump(self):
        self.is_jumping = True
        self.tick = 0
        self.y += 10
        self.set_sprite_sheet(t_player.jump_animation)

    def render(self, console, game):
        console.blit(self.get_sprite(), self.x, game.floor_height - 26 - self.y)
