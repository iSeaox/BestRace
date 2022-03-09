class Entity:
    """L'object Entity est une classe abstraite
    de laquelle vont dériver tout les ojects spécifiques
    à chaque entité comme le joueur, les oiseaux ou le mouton
    """

    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.tick = 0
        self.__sprite_sheet = None

    def do_tick(self):
        """Cette méthode doit être appeler à chaque fois que l'on veut
        passer à l'image suivante dans l'animation"""
        self.tick += 1
        self.tick %= len(self.__sprite_sheet)

    def render(self, console):
        raise NotImplementedError("render() method has to be overrid on child class")

    def get_sprite(self):
        """Cette méthode retourne l'image (appelée "sprite") à partir de la feuille de textures lié à l'object"""
        return self.__sprite_sheet[self.tick]

    def set_sprite_sheet(self, sprite_sheet):
        self.__sprite_sheet = sprite_sheet

    def get_sprite_sheet(self):
        return self.__sprite_sheet
