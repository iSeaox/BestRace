import time
import math

import keyboard

import display.console as console

import display.entity.sheep as sheep
import display.entity.player as player
import display.entity.bird as bird

import display.ui.score_renderer as score_renderer
import display.ui.string_renderer as string_renderer
from game.map.map import Map


class Game:
    """Cette classe représente le jeu et toute la gestion de celui-ci"""

    def __init__(self):
        self.__console = console.Console(100, 200)
        self.__map = Map()
        self.__map.max_pos = 200
        self.__map.min_pos = 100
        self.__run = True
        self.__frame_rate = 60
        self.floor_height = self.__console.height - 1

        self.__player = player.Player()

        self.score = 0

        self.__player.x = 3

    def game_loop(self):
        """Cette méthode lance la boucle qui fait tourner le jeu à chaque
        itération une nouvelle image est affichée à raison
        de self.__frame_rate par seconde"""
        tick = 0
        while(self.__run):
            begin = time.time_ns() / 1_000_000_000
            self.update()
            self.render(tick)

            rendered_console = self.__console.render()
            for line in rendered_console:
                print('\033[1A', end="")
            for line in rendered_console:
                print(line, end="")

            tick += 1
            tick %= 7
            elapsed = (time.time_ns() / 1_000_000_000 - begin)
            sleeping_time = (1 / self.__frame_rate) - elapsed
            # print(sleeping_time)
            if(sleeping_time > 0):
                time.sleep(sleeping_time)

    def update(self):
        """Cette méthode est appelée dans la boucle principale du jeu et permet
        de mettre à jour les objects. Elle s'appelle toujours avant de faire
        le rendu de l'image"""

        self.check_collision()

        self.__map.next_frame(self.__console)
        """
        if(self.__sheep.x + 20 < 0):
            self.__sheep.x = 250
            self.__sheepBis.x = 290
        self.__sheep.x -= 8
        self.__sheepBis.x -= 8
        self.__bird.x -= 5
        """
        self.score += 1

    def render(self, tick):
        """Cette méthode fait le rendu de la prochaine image qui va être affichée"""
        self.__console.clear_canvas()

        self.draw_floor()
        self.draw_score()
        self.draw_map()
        self.__console.blit(string_renderer.render_string("SWAG"), 50, 1)

    def trigger_key_event(self, event):
        """Est appelée par le gestionnaire de clavier lorsqu'une des touches écoutéés (voir keyboard_handler.py)
        et éxecute en fonction de l'évenement passse en paramètre l'action appropirée"""
        if(event.event_type == keyboard.KEY_DOWN):
            if(event.name == "haut" or event.name == "space"):
                if(not(self.__player.is_jumping)):
                    self.__player.jump()

    def check_collision(self):
        """Cette méthode vérifie qu'il n'y a pas de collision entre le joueur et une
        entité. Le cas échéant, elle retourne le type de l'entité touchée"""
        entities = self.__map.actual_frame.values
        for e in entities:
            if(e != self.__player):
                if(math.sqrt((e.x - self.__player.x) ** 2 + (e.y - self.__player.y) ** 2) < 40):
                    pass
                    # à finir

    def draw_floor(self):
        """Cette méthode s'éxécute dans le cadre du rendu de l'image, elle dessine le sol
        sur le canvas de la console"""
        floor = "██" * self.__console.width
        self.__console.blit(floor, 0, self.floor_height)

    def draw_score(self):
        """S'éxecute lors du rendu de l'image, elle permet de dessiner le score
        (self.score) sur le canvas de la console"""
        score_to_display = score_renderer.render_score(self.score)

        self.__console.blit(score_to_display, 1, 1)

    def draw_map(self):
        entities = self.__map.actual_frame
        self.__player.do_tick()
        self.__player.render(self.__console, self)
        for entity in entities.values:
            entity.do_tick()
            entity.render(self.__console, self)
