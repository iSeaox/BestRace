import keyboard

def enable(game):
    """Cette fonction permet d'activer la récupération des évenements claviers
    sur les touches up, space, down, shift et right"""

    keyboard.hook_key("up", game.trigger_key_event)
    keyboard.hook_key("space", game.trigger_key_event) # Les touches pour sauter

    keyboard.hook_key("down", game.trigger_key_event)
    keyboard.hook_key("shift", game.trigger_key_event) # Les touches pour se baisser

    keyboard.hook_key("right", game.trigger_key_event) # La touche pour taper
