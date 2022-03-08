import random
from display.entity.entity import Entity
from display.entity.sheep import BLACK_SHEEP, WHITE_SHEEP, Sheep


class Map:

    def __init__(self, console_width, console_height) -> None:
        self.__actual_frame = []
        self.__pos_next_objects = {}
        self.__cur_pos = (0, 0)
        self.__entities = [
            "white_sheep"
            "black_sheep",
            "bird"
        ]
        # le maximum de distance entre la position actuelle du joueur et le prochain obstacle
        self.max_pos = 100
        # idem mais le mini
        self.min_pos = 10
        self.console_width = console_width
        self.console_height = console_height

    def next_frame(self):
        self.__actual_frame = []
        if len(self.__pos_next_objects) == 0:
            self.__add_new_object()
        else:
            last_pos = self.__pos_next_objects.keys()[-1]
            last_entity = self.__pos_next_objects[last_pos]
            if last_pos[0] - self.__cur_pos < self.max_pos:
                self.__add_new_object()
            if last_pos[0] < self.__cur_pos:
                self.__pos_next_objects.pop(0)
        # for entity in self.__pos_next_objects.items():
        #    entity.x
        self.__cur_pos += 1
        return self.__actual_frame

    def create_map(self):
        self.next_frame()
        pass

    def __add_new_object(self):
        obj_pos = self.__cur_pos + random.randint(self.min_pos, self.max_pos)
        obj_name = random.choice(self.__entities)
        obj = None
        if(obj_name == "white_sheep"):
            obj = Sheep(WHITE_SHEEP)
        elif obj_name == "black_sheep":
            obj = Sheep(BLACK_SHEEP)
        else:
            obj = Entity()
        self.__pos_next_objects[(obj_pos, obj.y)] = obj
