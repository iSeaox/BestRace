import random
from display.entity.entity import Entity
from display.entity.sheep import BLACK_SHEEP, WHITE_SHEEP, Sheep


class Map:

    def __init__(self) -> None:
        """Crée la map automatiquement petit à petit.
        Après avoir appelé __init__, changez max_pos et min_pos si vous voulez puis appelez create_map pour initialiser la map."""
        # liste des entités actuels sur la map
        self.__pos_next_entities = {}
        # 1 pixel sur la console = 1 pos(ition)
        self.__cur_pos = 0
        # TO-DO: ajouter d'autres entités
        self.__entities = [
            "white_sheep"
            "black_sheep",
            "bird"
        ]
        # le maximum de distance entre la position actuelle du joueur et le prochain obstacle
        self.max_pos = 100
        # idem mais le mini
        self.min_pos = 10

    def next_frame(self):
        """Actualise la map en avançant les entités sur la map"""
        if len(self.__pos_next_entities) == 0:
            self.__add_new_entity()
        else:
            last_pos = self.__pos_next_entities.keys()[-1]
            #last_entity = self.__pos_next_entities[last_pos]
            if last_pos[0] - self.__cur_pos < self.max_pos:
                self.__add_new_entity()
            if last_pos[0] < self.__cur_pos:
                self.__pos_next_entities.pop(0)
        for i in self.__pos_next_entities.items():
            self.__pos_next_entities[i].x = i[0] - self.__cur_pos
        self.__cur_pos += 1
        return self.__pos_next_entities

    def create_map(self):
        """Initialise la map"""
        self.next_frame()
        pass

    def __add_new_entity(self):
        obj_pos = self.__cur_pos + random.randint(self.min_pos, self.max_pos)
        obj_name = random.choice(self.__entities)
        obj = None
        if(obj_name == "white_sheep"):
            obj = Sheep(WHITE_SHEEP)
        elif obj_name == "black_sheep":
            obj = Sheep(BLACK_SHEEP)
        else:
            obj = Entity()
        self.__pos_next_entities[(obj_pos, obj.y)] = obj
