import display.entity.entity as entity

import textures.player as t_player

class Player(entity.Entity):

    def __init__(self, floor_height):
        super().__init__() # permet d'appeller le constructeur de la superclass
        # ici entity.Entity
        self.floor_height = floor_height - 26
        self.y = self.floor_height
        self.is_jumping = False
        self.jump_height = 25
        self.set_sprite_sheet(t_player.player_animation)

    def do_tick(self):
        """Cette méthode est systématiquement appelée avant le rendu elle
        permet de mettre à jour toutes les propriétés liées au joueur"""
        if(self.is_jumping):
            if(self.tick == len(self.get_sprite_sheet()) - 1):
                self.is_jumping = False
                self.y = self.floor_height
                self.set_sprite_sheet(t_player.player_animation)
            elif(self.tick == len(self.get_sprite_sheet()) - 2):
                self.y = self.floor_height - self.jump_height // 4
            else:
                self.y = self.floor_height - self.jump_height
        self.tick += 1
        self.tick %= len(self.get_sprite_sheet())

    def jump(self):
        """Intialiase le saut"""
        self.is_jumping = True
        self.tick = 0
        self.set_sprite_sheet(t_player.jump_animation)

    def render(self, console, game):
        """Permet de faire le rendu du joueur dans l'object console"""
        console.blit(self.get_sprite(), self.x, self.y)
