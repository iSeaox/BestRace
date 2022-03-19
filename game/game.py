import time
import math

import keyboard

import display.console as console

import display.entity.sheep as sheep
import display.entity.player as player
import display.entity.bird as bird
import display.entity.background as background
import display.entity.moon as moon

import display.ui.score_renderer as score_renderer
import display.ui.string_renderer as string_renderer
from game.map.map import Map

import textures.ui.menu as t_menu

import utils.storage_handler as s_handler


class Game:
    """Cette classe représente le jeu et toute la gestion de celui-ci"""

    def __init__(self):
        self.__console = console.Console(100, 200)
        self.__map = Map()
        self.__map.max_pos = 100
        self.__map.min_pos = 50
        self.__run = False
        self.__frame_rate = 20
        self.__in_menu = False
        self.floor_height = self.__console.height - 1

        self.__player = player.Player(self.floor_height)

        self.__background1 = background.Background()
        self.__background2 = background.Background()
        self.__background2.x = 288
        self.__moon1 = moon.Moon()
        self.__moon2 = moon.Moon()
        self.__moon1.x = 171
        self.__moon2.x = 459

        self.score = 0

        self.__player.x = 3

    def open_menu(self, last_score=None):
        self.__in_menu = True

        self.__console.blit(t_menu.left_up_corner, 0, 0)
        self.__console.blit(t_menu.right_up_corner, self.__console.width - 11, 0)

        self.__console.blit(t_menu.right_down_corner, self.__console.width - 11, self.__console.height - 12)
        self.__console.blit(t_menu.left_down_corner, 0, self.__console.height - 12)

        title = string_renderer.render_string("BESTRACE !")
        self.__console.blit(title, self.__console.width // 2 - 20, 5)

        scores = s_handler.get_scores()
        self.__console.blit(t_menu.score_border, 85, 20)
        self.__console.blit(string_renderer.render_string("SCORE"), 88, 23)

        score_to_display = 5
        i = 1
        while(i <= score_to_display):
            if(i <= len(scores)):
                self.__console.blit(string_renderer.render_string(str(i) + ": " + str(scores[i - 1])), 85, 33 + (i * 6))
            i += 1


        self.__console.blit(string_renderer.render_string("PENSEZ A AJUSTER LA FENETRE AVEC LES COINS"), 5, self.__console.height - 10)

        rendered_console = self.__console.render()
        for line in rendered_console:
            print('\033[1A', end="")
        for line in rendered_console:
            print(line, end="")

        while(self.__in_menu):
            pass
        self.__run = True

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

        self.__background1.do_tick()
        self.__background2.do_tick()
        self.__moon1.do_tick()
        self.__moon2.do_tick()

        self.__map.next_frame(self.__console)

        self.score += 1

    def render(self, tick):
        """Cette méthode fait le rendu de la prochaine image qui va être affichée"""
        self.__console.clear_canvas()

        self.__background1.render(self.__console, self)
        self.__background2.render(self.__console, self)
        self.__moon1.render(self.__console, self)
        self.__moon2.render(self.__console, self)

        self.draw_floor()
        self.draw_score()
        self.draw_map()
        self.__console.blit(string_renderer.render_string("L'NSI : LA MEILLEURE DES MATIERES"), 20, 2)

    def trigger_key_event(self, event):
        """Est appelée par le gestionnaire de clavier lorsqu'une des touches écoutéés (voir keyboard_handler.py)
        et éxecute en fonction de l'évenement passse en paramètre l'action appropirée"""
        if(event.event_type == keyboard.KEY_DOWN):
            if(event.name == "haut" or event.name == "space"):
                if(self.__in_menu):
                    self.__in_menu = False
                else:
                    if(not(self.__player.is_jumping)):
                        self.__player.jump()

    def check_collision(self):
        """Cette méthode vérifie qu'il n'y a pas de collision entre le joueur et une
        entité. Le cas échéant, elle retourne le type de l'entité touchée"""
        entities = self.__map.actual_frame.get_values()

        player_pixel_positions = self.__player.get_pixel_positions()

        for e in entities:
            if(e != self.__player):
                if(math.sqrt((e.x - self.__player.x) ** 2 + (e.y - self.__player.y) ** 2) < 40):
                    e_pixel_positions = e.get_pixel_positions()
                    for pp_pos in player_pixel_positions:
                        if(pp_pos in e_pixel_positions):
                            self.__run = False
                    # print("\n ENTITY" + str(e_pixel_positions), len(e_pixel_positions))
                    # print("\n PLAYER:" + str(player_pixel_positions), len(player_pixel_positions))



    def draw_floor(self):
        """Cette méthode s'éxécute dans le cadre du rendu de l'image, elle dessine le sol
        sur le canvas de la console"""
        floor = "██" * self.__console.width
        self.__console.blit(floor, 0, self.floor_height)

    def draw_score(self):
        """S'éxecute lors du rendu de l'image, elle permet de dessiner le score
        (self.score) sur le canvas de la console"""
        score_to_display = score_renderer.render_score(self.score)
        self.__console.blit(score_to_display, 1, 2)

    def draw_map(self):
        entities = self.__map.actual_frame
        self.__player.do_tick()
        self.__player.render(self.__console, self)
        for entity in entities.get_values():
            entity.do_tick()
            entity.render(self.__console, self)
