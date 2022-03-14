import time
import math

import keyboard

import display.console as console
import display.entity.sheep as sheep
import display.entity.player as player
import display.entity.bird as bird
import display.ui.score_renderer as score_renderer



class Game:
    """Cette classe représente le jeu et toute la gestion de celui-ci"""
    def __init__(self):
        self.__console = console.Console(60, 200)
        self.__run = True
        self.__frame_rate = 2
        self.floor_height = self.__console.height - 1

        self.__sheep = sheep.Sheep(sheep.BLACK_SHEEP)
        self.__sheepBis = sheep.Sheep(sheep.WHITE_SHEEP)
        self.__player = player.Player()
        self.__bird = bird.Bird()

        self.entities = []
        self.entities.append(self.__sheep)
        self.entities.append(self.__sheepBis)
        self.entities.append(self.__bird)
        self.entities.append(self.__player)

        self.score = 0

        self.__player.x = 3
        self.__sheep.x = 250
        self.__sheepBis.x = 260
        self.__bird.x = 200
        self.__bird.y = 10

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

        if(self.__sheep.x + 20 < 0):
            self.__sheep.x = 250
            self.__sheepBis.x = 260
        self.__sheep.x -= 8
        self.__sheepBis.x -= 8
        self.__bird.x -= 5

        self.__player.do_tick()
        self.__sheep.do_tick()
        self.__sheepBis.do_tick()
        self.__bird.do_tick()

    def render(self, tick):
        """Cette méthode fait le rendu de la prochaine image qui va être affichée"""
        self.__console.clear_canvas()

        self.__player.render(self.__console, self)
        self.__sheep.render(self.__console, self)
        self.__sheepBis.render(self.__console, self)
        self.__bird.render(self.__console, self)
        self.draw_floor()

    def check_collision(self):
        """Cette méthode vérifie qu'il n'y a pas de collision entre le joueur et une
        entité. Le cas échéant, elle retourne le type de l'entité touchée"""
        for e in self.entities:
            if(e != self.__player):
                if(math.sqrt((e.x - self.__player.x) ** 2 + (e.y - self.__player.y) ** 2) < 40):
                    pass

    def trigger_key_event(self, event):
        """Est appelée par le gestionnaire de clavier lorsqu'une des touches écoutéés (voir keyboard_handler.py)
        et éxecute en fonction de l'évenement passse en paramètre l'action appropirée"""
        if(event.event_type == keyboard.KEY_DOWN):
            if(event.name == "haut" or event.name == "space"):
                if(not(self.__player.is_jumping)):
                    self.__player.jump()

    def draw_floor(self):
        """Cette méthode s'éxécute dans le cadre du rendu de l'image, elle dessine le sol
        sur le canvas de la console"""
        floor = "██" * self.__console.width
        self.__console.blit(floor, 0, self.floor_height)
