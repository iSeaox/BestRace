import display.entity.entity as entity

import textures.player as t_player

class Player(entity.Entity):

    def __init__(self, floor_height):
        super().__init__() # permet d'appeller le constructeur de la superclass
        # ici entity.Entity
        self.floor_height = floor_height
        self.y = self.floor_height - 26
        self.is_jumping = False
        self.is_mandaling = False
        self.is_kroutchev = False
        self.jump_height = 25
        self.selected_skin = 0
        self.set_sprite_sheet(t_player.player_skins[self.selected_skin]["player_animation"])

    def do_tick(self):
        """Cette méthode est systématiquement appelée avant le rendu elle
        permet de mettre à jour toutes les propriétés liées au joueur"""
        if(self.is_mandaling):
            if(self.tick == len(self.get_sprite_sheet()) - 1):
                self.is_mandaling = False
                self.set_sprite_sheet(t_player.player_skins[self.selected_skin]["player_animation"])

        if(self.is_kroutchev):
            if(self.tick == len(self.get_sprite_sheet()) - 1):
                self.is_kroutchev = False
                self.set_sprite_sheet(t_player.player_skins[self.selected_skin]["player_animation"])
                self.y -= 6

        if(self.is_jumping):
            if(self.tick == len(self.get_sprite_sheet()) - 1):
                self.is_jumping = False
                self.y = self.floor_height
                self.set_sprite_sheet(t_player.player_skins[self.selected_skin]["player_animation"])
            elif(self.tick == len(self.get_sprite_sheet()) - 2):
                self.y = self.floor_height - self.jump_height // 4
            else:
                self.y = self.floor_height - self.jump_height
        self.tick += 1
        self.tick %= len(self.get_sprite_sheet())

    def do_mandale(self):
        """Intialiase la mandale"""
        if(self.is_kroutchev):
            self.is_kroutchev = False
            self.y -= 6
        self.is_mandaling = True
        self.tick = 0
        self.set_sprite_sheet(t_player.player_skins[self.selected_skin]["mandale_animation"])

    def jump(self):
        """Intialiase le saut"""
        self.is_jumping = True
        self.tick = 0
        self.set_sprite_sheet(t_player.player_skins[self.selected_skin]["jump_animation"])
        self.is_mandaling = False

    def do_crouch(self):
        if not self.is_jumping and not self.is_kroutchev:
            self.is_kroutchev = True
            self.tick = 0
            self.set_sprite_sheet(t_player.player_skins[self.selected_skin]["crouch_animation"])
            self.is_mandaling = False
            self.y += 6

    def render(self, console, game):
        """Permet de faire le rendu du joueur dans l'object console"""
        console.blit(self.get_sprite(), self.x, self.y)

    def get_skins(self):
        return [t_player.player_skins[0]["player_animation"][0], t_player.player_skins[1]["player_animation"][0], t_player.player_skins[2]["player_animation"][0]]

    def set_selected_skin(self, selected):

        # if selected != self.selected_skin:
        #     if self.selected_skin == 2:
        #         self.floor_height += 3
        #         self.y = self.floor_height
        #     else:
        #         self.floor_height -= 3
        #         self.y = self.floor_height

        self.selected_skin = selected
        self.set_sprite_sheet(t_player.player_skins[self.selected_skin]["player_animation"])
        temp_height = len(self.get_sprite_sheet()[0].split("\n")) - 1
        self.y = self.floor_height - temp_height
        self.floor_height -= temp_height
