import random
from display.console import Console
from display.entity.bird import Bird
from display.entity.entity import Entity
from display.entity.sheep import BLACK_SHEEP, WHITE_SHEEP, Sheep
from game.map.listoflist import ListOfList


class Map:

    def __init__(self) -> None:
        """Crée la map automatiquement petit à petit.
        Après avoir appelé __init__, changez max_pos et min_pos si vous voulez puis appelez create_map pour initialiser la map."""
        # liste des entités actuels sur la map
        self.actual_frame = ListOfList()
        # 1 pixel sur la console = 1 pos(ition)
        self.__cur_pos = 0
        # TO-DO: ajouter d'autres entités
        self.__entities = [
            "white_sheep",
            "black_sheep",
            "bird"
        ]
        # le maximum de distance entre la position actuelle du joueur et le prochain obstacle
        self.max_pos = 100
        # idem mais le mini
        self.min_pos = 10
        # chance d'apparition pour chaque entités / le nombre total de "pourcentage"
        self.perc_bird = 10
        self.perc_white_sheep = 45
        self.perc_black_sheep = 45
        #
        self.__percentage = [0 for i in range(self.perc_white_sheep)] \
            + [1 for i in range(self.perc_black_sheep)] \
            + [2 for i in range(self.perc_bird)]

    def next_frame(self, console: Console):
        """Actualise la map en avançant les entités sur la map"""
        if len(self.actual_frame) == 0:
            self.__add_new_entity(console)
        else:
            last_pos = self.actual_frame.get_keys()[-1]
            last_entity = self.actual_frame[last_pos]
            if last_entity.x + last_entity.width < console.width:
                self.__add_new_entity(console)
        for i in self.actual_frame.get_keys():
            entity = self.actual_frame[i]
            if entity.x + entity.width < 0:
                self.actual_frame.pop(0)
            else:
                entity.x = i[0] - self.__cur_pos
        self.__cur_pos += 1
        return self.actual_frame

    def create_map(self):
        """Initialise la map"""
        self.next_frame()
        pass

    def __add_new_entity(self, console: Console):
        obj_pos = self.__cur_pos + console.width + \
            random.randint(self.min_pos, self.max_pos)
        index = self.__percentage[random.randint(0, len(self.__percentage)-1)]
        obj_name = self.__entities[index]
        obj = None
        if(obj_name == "white_sheep"):
            obj = Sheep(WHITE_SHEEP)
        elif obj_name == "black_sheep":
            obj = Sheep(BLACK_SHEEP)
        else:
            obj = Bird()
        self.actual_frame.append((obj_pos, obj.y), obj)
        #self.actual_frame[(obj_pos, obj.y)] = obj
