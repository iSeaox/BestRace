class Entity:
    """L'object Entity est une classe abstraite
    de laquelle vont dériver tout les ojects spécifiques
    à chaque entité comme le joueur, les oiseaux ou les moutons
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
        raise NotImplementedError(
            "render() method has to be overrid on child class")

    def get_pixel_positions(self):
        """Retourne la liste des positions de tout les pixel blanc de l'entités sous la forme
        d'une liste de tupe (y, x)"""
        pixel_positions = []
        t_splited = self.get_sprite().split("\n")
        for line_index in range(len(t_splited)):
            pixel_index = 0
            while(pixel_index < len(t_splited[line_index])):
                if(t_splited[line_index][pixel_index:(pixel_index + 2)] == "██"):
                    pixel_positions.append((self.y + line_index, self.x + (pixel_index // 2)))
                pixel_index += 2
        return pixel_positions

    def get_sprite(self):
        """Cette méthode retourne l'image (appelée "sprite") à partir de la feuille de textures lié à l'object"""
        sprite = self.__sprite_sheet[self.tick]
        self.width = max(len(i) for i in sprite.split("\n")) // 2
        self.height = len(sprite.split("\n")) - 2
        return sprite

    def set_sprite_sheet(self, sprite_sheet: list):
        self.__sprite_sheet = sprite_sheet

    def get_sprite_sheet(self):
        return self.__sprite_sheet
