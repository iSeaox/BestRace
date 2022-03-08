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
        self.__sheep = sheep.Sheep(sheep.WHITE_SHEEP)
        self.__sheepBis = sheep.Sheep(sheep.BLACK_SHEEP)
        self.__sheep.x += 60
        self.__sheepBis.x += 30

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
        self.__sheep.do_tick()
        self.__sheepBis.do_tick()

    def render(self, tick):
        self.__console.clear_canvas()
        self.__console.blit(player[tick], 0, self.floor_height - 25)
        self.__sheep.render(self.__console, self)
        self.__sheepBis.render(self.__console, self)
        self.draw_floor()

    def draw_floor(self):
        floor = "██" * self.__console.width
        self.__console.blit(floor, 0, self.floor_height)
