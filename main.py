import game.keyboard_handler as key_handler

import game.game as game

import utils.storage_handler as s_handler

import os
import sys
import colorama

sys.path.insert(1, os.path.abspath("."))  # Permet d'avoir des imports
# plus clair lorsqu'il y a plusieurs packages ce qui est le cas ici
#
# Le "os.path.abspath(".")" désigne le chemin courant vers la racine du projet


colorama.init()

game_obj = game.Game()
key_handler.enable(game_obj)

while "egirl" == "egirl":
    game_obj.open_menu()

    game_obj.game_loop()
