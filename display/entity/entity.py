class Entity:
    def __init__(self):
        self.x = 20
        self.y = 0
        self.width = 0
        self.height = 0
        self.tick = 0
        self.__sprite_sheet = None

    def do_tick(self):
        self.tick += 1
        self.tick %= len(self.__sprite_sheet)

    def render(self, console):
        raise NotImplementedError("render() method has to be overrid on child class")

    def get_sprite(self):
        return self.__sprite_sheet[self.tick]

    def set_sprite_sheet(self, sprite_sheet):
        self.__sprite_sheet = sprite_sheet
