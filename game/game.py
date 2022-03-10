import time

import keyboard

import display.console as console
import display.entity.sheep as sheep
import display.entity.player as player


class Game:
    """Cette classe représente le jeu et toute la gestion de celui-ci"""
    def __init__(self):
        self.__console = console.Console(60, 150)
        self.__run = True
        self.__frame_rate = 30
        self.floor_height = self.__console.height - 1

        self.__sheep = sheep.Sheep(sheep.BLACK_SHEEP)
        self.__sheepBis = sheep.Sheep(sheep.WHITE_SHEEP)
        self.__player = player.Player()

        self.__player.x = 3
        self.__sheep.x = 150
        self.__sheepBis.x = 160

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
                print(line, end="")

            tick += 1
            tick %= 7
            elapsed = (time.time_ns() / 1_000_000_000 - begin)
            sleeping_time = (1 / self.__frame_rate) - elapsed
            # print(sleeping_time)
            if(sleeping_time > 0):
                time.sleep(sleeping_time)

    def update(self):
        if(self.__sheep.x + 20 < 0):
            self.__sheep.x = 150
            self.__sheepBis.x = 160
        self.__sheep.x -= 8
        self.__sheepBis.x -= 8

        self.__player.do_tick()
        self.__sheep.do_tick()
        self.__sheepBis.do_tick()

    def render(self, tick):
        self.__console.clear_canvas()

        self.__player.render(self.__console, self)
        self.__sheep.render(self.__console, self)
        self.__sheepBis.render(self.__console, self)
        self.draw_floor()

    def trigger_key_event(self, event):
        if(event.event_type == keyboard.KEY_DOWN):
            if(event.name == "haut" or event.name == "space"):
                if(not(self.__player.is_jumping)):
                    self.__player.jump()

    def draw_floor(self):
        floor = "██" * self.__console.width
        self.__console.blit(floor, 0, self.floor_height)
