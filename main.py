import os
import sys
import colorama

sys.path.insert(1, os.path.abspath(".")) # Permet d'avoir des imports
# plus clair lorsqu'il y a plusieurs packages ce qui est le cas ici
#
# Le "os.path.abspath(".")" désigne le chemin courant vers la racine du projet

import game.game as game
import game.keyboard_handler as key_handler

colorama.init()

game_obj = game.Game()
key_handler.enable(game_obj)

game_obj.game_loop()
