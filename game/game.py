import time

import display.console as console
from textures.player import player_animation as player

sheep = """
      ██████████
    ██          ██
    ██            ██
      ████          ██
    ██    ██          ████          ████████
  ██                      ██████████        ████
██    ██                                        ██
██                                              ██
  ██        ██                                    ██
    ████████                                      ██
        ██                                        ██
        ██                                        ██
          ██                                      ██
          ██                                      ██
            ██                                  ██
              ██                                ██
              ██                            ████
                ██      ████████████      ██
                  ██  ██            ██    ██
                  ██  ██              ██  ██
                ██    ██            ██    ██
                ██████              ██████
"""

sheep_blanc = """
      ██████████
    ██████████████
    ████████████████
      ████████████████
    ██    ████████████████          ████████
  ██            ████████████████████████████████
██    ██        ██████████████████████████████████
██            ████████████████████████████████████
  ██        ████████████████████████████████████████
    ████████████████████████████████████████████████
        ████████████████████████████████████████████
        ████████████████████████████████████████████
          ██████████████████████████████████████████
          ██████████████████████████████████████████
            ██████████████████████████████████████
              ████████████████████████████████████
              ██████████████████████████████████
                ██      ██████████████    ██
                  ██  ██            ██    ██
                  ██  ██              ██  ██
                ██    ██            ██    ██
                ██████              ██████
"""


class Game:

    def __init__(self):
        self.__console = console.Console(60, 100)
        self.__run = True
        self.__frame_rate = 100

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
        self.__console.blit(sheep, 51, 1)
        self.__console.blit(player[tick], 10, 0)
        self.__console.blit(sheep_blanc, 60, 5)
        self.__console.blit(sheep_blanc, 80, 0)
