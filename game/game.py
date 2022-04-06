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
from game.challenges_handler import ChallengesHandler
from game.map.map import Map
from game.penality_handler import PenalityHandler

import textures.ui.menu as t_menu
import textures.ui.key as t_key

import utils.storage_handler as s_handler


class Game:
    """Cette classe représente le jeu et toute la gestion de celui-ci"""

    def __init__(self):
        self.__console = console.Console(125, 200)
        self.__map = Map()
        self.__map.entity_disappear = self.trigger_sheep_event
        self.__map.max_pos = 100
        self.__map.min_pos = 50
        self.__run = False
        self.__frame_rate = 30

        self.__in_menu = False
        self.__in_menu_stat = False
        self.__selected_skin_id = 0

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
        self.__last_score = None
        self.__frames = 0

        self.__player.x = 3

        self.curent_penality = PenalityHandler()
        self.challenges = ChallengesHandler()
        self.create_challenges()

    def open_menu(self, last_score=None):
        """ouvre le menu qui s'affiche avant le jeu et bloque le thread jusqu'à ce
        que le joueur appuie sur espace"""
        self.__in_menu = True

        while(self.__in_menu):
            self.__console.clear_canvas()

            self.__console.blit(t_menu.left_up_corner, 0, 0)
            self.__console.blit(t_menu.right_up_corner,
                                self.__console.width - 11, 0)

            self.__console.blit(t_menu.right_down_corner,
                                self.__console.width - 11, self.__console.height - 12)
            self.__console.blit(t_menu.left_down_corner, 0,
                                self.__console.height - 12)

            title = string_renderer.render_string("BESTRACE !")
            self.__console.blit(title, self.__console.width // 2 - 20, 5)

            if(not(self.__in_menu_stat)):
                scores = s_handler.get_scores()
                self.__console.blit(t_menu.score_border, 85, 20)
                self.__console.blit(string_renderer.render_string("SCORE"), 88, 23)

                score_to_display = 5
                i = 1
                while(i <= score_to_display):
                    if(i <= len(scores)):
                        self.__console.blit(string_renderer.render_string(
                            str(i) + ": " + str(scores[i - 1]) + (" VOUS" if scores[i - 1] == self.__last_score else "")), 85, 33 + (i * 6))
                    i += 1

                self.__console.blit(string_renderer.render_string("APPUYEZ SUR ENTRER POUR ACCEDER AU MENU"), 8, self.__console.height - 10)
            else:
                subtitle_chal = string_renderer.render_string("CHALLENGES:")
                self.__console.blit(subtitle_chal, 7, 12)

                cursor_y = 0
                for chal_key in self.challenges.get_all_challenges_id():
                    if(not(self.challenges.have_completed_challenge(chal_key))):
                        chal_name = self.challenges.get_challenge_name(chal_key)

                        str_chal = string_renderer.render_string("* " + chal_name.upper())
                        self.__console.blit(str_chal, 12, 20 + cursor_y)

                        cursor_y += 7

                subtitle_skin = string_renderer.render_string("SKINS:")
                self.__console.blit(subtitle_skin, 7, 70)
                self.__console.blit(t_key.left_arrow, 70, 105)
                self.__console.blit(t_key.right_arrow, self.__console.width - 70, 105)

                skins = self.__player.get_skins()
                if(self.__selected_skin_id < 0):
                    self.__selected_skin_id = len(skins) - 1
                self.__selected_skin_id %= len(skins)

                current_skin = skins[self.__selected_skin_id]
                self.__console.blit(current_skin, 94, 80)


            rendered_console = self.__console.render()
            for line in rendered_console:
                print('\033[1A', end="")
            for line in rendered_console:
                print(line, end="")

            time.sleep(0.0001 / self.__frame_rate)
        self.__run = True
        self.__in_menu_stat = False
        self.__player.set_selected_skin(self.__selected_skin_id)

    def game_loop(self):
        """Cette méthode lance la boucle qui fait tourner le jeu à chaque
        itération une nouvelle image est affichée à raison
        de self.__frame_rate par seconde"""
        tick = 0
        while(self.__run):
            begin = time.time_ns() / 1_000_000_000
            self.update()
            if(not(self.__run)):
                break  # Ferme le jeu sans afficher l'image suivante dans le cas des collisions par exemple
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

        stricken_entity = self.check_collision()
        if(stricken_entity != None):
            if(isinstance(stricken_entity, sheep.Sheep) and stricken_entity.get_color() == sheep.BLACK_SHEEP):
                if(self.__player.is_mandaling):
                    self.__map.actual_frame.pop(0)
                    self.challenges.add_challenge_counter("Black_sheep", False)
                else:
                    self.reset_game()
            else:
                self.reset_game()

        self.__background1.do_tick()
        self.__background2.do_tick()
        self.__moon1.do_tick()
        self.__moon2.do_tick()

        self.__map.next_frame(self.__console)

        self.score += 1

        self.__map.speed = self.__frames // 200
        if self.curent_penality.get_current_penality_type() == "speed_game" and self.__frames < self.curent_penality.get_current_penality_frame_stop():
            self.__map.speed += self.curent_penality.get_current_penality_value()
        self.__frames += 1

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
        # self.__console.blit(string_renderer.render_string("L'NSI : LA MEILLEURE DES MATIERES"), 20, 2)

    def trigger_key_event(self, event):
        """Est appelée par le gestionnaire de clavier lorsqu'une des touches écoutées (voir keyboard_handler.py)
        et exécute en fonction de l'évenement passé en paramètre l'action appropriée"""
        if(event.event_type == keyboard.KEY_DOWN):
            if(event.name == "haut" or event.name == "space"):
                if(self.__in_menu):
                    self.__in_menu = False
                else:
                    if(not(self.__player.is_jumping)):
                        self.__player.jump()
            elif(event.name == "droite"):
                if(not(self.__in_menu) and not(self.__player.is_jumping) and not(self.__player.is_mandaling)):
                    self.__player.do_mandale()
                elif(self.__in_menu and self.__in_menu_stat):
                    self.__selected_skin_id += 1

            elif(event.name == "gauche"):
                if(self.__in_menu and self.__in_menu_stat):
                    self.__selected_skin_id -= 1

            elif(event.name == "bas"):
                if(not(self.__in_menu) and not(self.__player.is_jumping)):
                    self.__player.do_crouch()
            elif(event.name == "enter"):
                if(self.__in_menu):
                    self.__in_menu_stat = True

    def trigger_sheep_event(self, entity):
        """Est appelée par le gestionnaire de la carte lorsqu'une entitée sort de l'écran du jeu (voir map/map.py)"""
        if(type(entity) == sheep.Sheep and entity.get_color() == sheep.BLACK_SHEEP):
            self.curent_penality.set_penality(self.__frames + 100)
            if self.curent_penality.get_current_penality_type() == "lost_pts":
                if self.score < self.curent_penality.get_current_penality_value():
                    self.score = 0
                else:
                    self.score -= self.curent_penality.get_current_penality_value()
        elif type(entity) == sheep.Sheep and entity.get_color() == sheep.WHITE_SHEEP:
            self.challenges.add_challenge_counter("White_sheep", False)
        else:
            self.challenges.add_challenge_counter("Avoid_pigeons", False)

    def check_collision(self):
        """Cette méthode vérifie qu'il n'y a pas de collision entre le joueur et une
        entité. Le cas échéant, elle retourne l'entité touchée par le joueur"""
        entities = self.__map.actual_frame.get_values()
        player_pixel_positions = self.__player.get_pixel_positions()
        for e in entities:
            if(e != self.__player):
                if(math.sqrt((e.x - self.__player.x) ** 2 + (e.y - self.__player.y) ** 2) < 40):
                    e_pixel_positions = e.get_pixel_positions()
                    for pp_pos in player_pixel_positions:
                        if(pp_pos in e_pixel_positions):
                            return e

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
        """Cette méthode s'éxécute dans le cadre du rendu de l'image, elle dessine toutes les entitées de la
        map sur le canvas de la console"""
        entities = self.__map.actual_frame
        self.__player.do_tick()
        self.__player.render(self.__console, self)
        for entity in entities.get_values():
            entity.do_tick()
            entity.render(self.__console, self)

    def reset_game(self):
        s_handler.store_new_score(self.score)
        self.challenges.set_challenge_counter("Reach_pts", self.score, False)
        self.challenges.set_challenge_counter(
            "Reach_pts_total", self.challenges.get_challenge_state("Reach_pts_total") + self.score, False)
        # MONTRER LES PENALITES SEULEMENT ICI. Après ce commentaire, les défis sont réinitialisés
        self.reset_one_time_challenges()
        self.challenges.write_file()
        self.__last_score = self.score
        self.score = 0
        self.__frames = 0
        self.curent_penality.reset_penality()
        self.__player.tick = 0
        self.__console.clear_canvas()
        self.__map.reset_map()
        self.__run = False

    def reset_one_time_challenges(self):
        self.challenges.reset_challenge("Reach_pts", False)
        self.challenges.reset_challenge("Avoid_penalities", False)
        self.challenges.reset_challenge("I_love_penalities", False)

    def create_challenges(self):
        self.challenges.create_challenge(
            "Reach_pts", "Atteindre GOAL points en une partie", 750)
        self.challenges.create_challenge(
            "Reach_pts_total", "Atteindre GOAL points au total", 4000)
        self.challenges.create_challenge(
            "White_sheep", "Eviter GOAL moutons blancs au total", 150)
        self.challenges.create_challenge(
            "Black_sheep", "Percuter GOAL moutons noirs au total", 300)
        self.challenges.create_challenge(
            "Avoid_pigeons", "Eviter GOAL pigeons au total", 75)
        self.challenges.create_challenge(
            "Avoid_penalities", "GOAL penalites en une partie", 0)
        self.challenges.create_challenge(
            "I_love_penalities", "Prendre GOAL penalites en une partie", 10)
