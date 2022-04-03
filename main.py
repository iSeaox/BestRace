import game.keyboard_handler as key_handler

import game.game as game

import utils.storage_handler as s_handler

import os
import sys
import colorama
import ctypes

# Modifier la taille de la police d'écriture
LF_FACESIZE = 32
STD_OUTPUT_HANDLE = -11


class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]


class CONSOLE_FONT_INFOEX(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_ulong),
                ("nFont", ctypes.c_ulong),
                ("dwFontSize", COORD),
                ("FontFamily", ctypes.c_uint),
                ("FontWeight", ctypes.c_uint),
                ("FaceName", ctypes.c_wchar * LF_FACESIZE)]


font = CONSOLE_FONT_INFOEX()
font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
font.dwFontSize.Y = 5
font.FaceName = "Lucida Console"

handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
ctypes.windll.kernel32.SetCurrentConsoleFontEx(
    handle, ctypes.c_long(False), ctypes.pointer(font))
#

sys.path.insert(1, os.path.abspath("."))  # Permet d'avoir des imports
# plus clair lorsqu'il y a plusieurs packages ce qui est le cas ici
#
# Le "os.path.abspath(".")" désigne le chemin courant vers la racine du projet


colorama.init()

# Modifier la taille de la fenêtre
cmd = 'mode 400,101'
os.system(cmd)
#

game_obj = game.Game()
key_handler.enable(game_obj)

while "egirl" == "egirl":
    game_obj.open_menu()

    game_obj.game_loop()
