class Entity:
    def __init__(self):
        self.x = 5
        self.y = 0
        self.width = 0
        self.height = 0
        self.tick = 0
        self.__sprite_sheet = ""

    def tick(self):
        self.tick += 1
        self.tick %= len(self.__sprite_sheet)

    def render(self, console):
        raise NotImplementedError("render() method has to be overrid on child class")

    def get_sprite(self, index):
        return self.__sprite_sheet[index]
