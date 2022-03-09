import os
import sys
sys.path.insert(1, os.path.abspath("."))

import game.game as game
import game.keyboard_handler as key_handler

game_obj = game.Game()
key_handler.enable(game_obj)
while(1):
    pass
#game_obj.game_loop()
