import time

import display.console as console
import display.entity.sheep as sheep
from textures.player import player_animation as player


class Game:

    def __init__(self):
        self.__console = console.Console(50, 110)
        self.__run = True
        self.__frame_rate = 5
        self.floor_height = self.__console.height - 1
        self.__sheep = sheep.Sheep(sheep.BLACK_SHEEP)

    def game_loop(self):
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
            print(sleeping_time)
            if(sleeping_time > 0):
                time.sleep(sleeping_time)

    def update(self):
        pass

    def render(self, tick):
        self.__console.clear_canvas()

        self.__sheep.render(self.__console, self)
        self.draw_floor()

    def draw_floor(self):
        floor = "██" * self.__console.width
        self.__console.blit(floor, 0, self.floor_height)
