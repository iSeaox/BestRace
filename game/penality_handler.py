import random as rdm


class PenalityHandler:
    def __init__(self) -> None:
        self.__penality_type = None
        self.__value = 0
        self.__frame_stop = -1

    def set_penality(self, frame_stop):
        penalities = [
            "speed_game",
            "lost_pts"
        ]
        penality = rdm.choice(penalities)
        self.__penality_type = penality
        if penality == "speed_game":
            self.__value = 3
            self.__frame_stop = frame_stop
        elif penality == "lost_pts":
            self.__value = 200
        else:
            raise IndexError(
                "This penality is not handled by the game. Penality : " + penality)

    def get_current_penality_type(self):
        return self.__penality_type

    def get_current_penality_value(self):
        return self.__value

    def get_current_penality_frame_stop(self):
        return self.__frame_stop

    def reset_penality(self):
        self.__penality_type = None
        self.__value = 0
        self.__frame_stop = -1
