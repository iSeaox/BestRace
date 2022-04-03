import json
import os


class ChallengesHandler:
    def __init__(self) -> None:
        self.__FILE_PATH = os.path.abspath(".") + "\\data\\challenges.json"
        """Gestionnaire de défis."""
        with open(self.__FILE_PATH, "a+") as file:
            file.seek(0)
            try:
                self.__challenges_user = json.loads(file.readlines()[0])
            except:
                self.__challenges_user = {}
        self.__challenges_info = {}

    def add_challenge_counter(self, challenge_id, autowrite=True):
        """Ajouter un point sur un défi en donnant son identifiant"""
        self.__challenges_user[challenge_id] += 1
        if autowrite:
            self.write_file()

    def set_challenge_counter(self, challenge_id, counter, autowrite=True):
        self.__challenges_user[challenge_id] = counter
        if autowrite:
            self.write_file()

    def create_challenge(self, challenge_id: str, name: str, goal: int):
        """Créer un défi en lui donnant un id, un nom et un but à atteindre.
        Utiliser "GOAL" dans le nom permet d'avoir le objectif dans le nom du défi en utilisant get_challenge_name"""
        self.__challenges_info[challenge_id] = {"name": name, "goal": goal}
        self.__challenges_user[challenge_id] = 0

    def reset_challenge(self, challenge_id, autowrite=True):
        """Réinitialiser un des défis selon son identifiant"""
        self.__challenges_user[challenge_id] = 0
        if autowrite:
            self.write_file()

    def reset_all(self):
        """Réinitialiser tous les défis"""
        self.__challenges_user = {}
        self.write_file()

    def get_challenge_state(self, challenge_id):
        """Savoir l'avancement d'un défi selon son identifiant"""
        return self.__challenges_user[challenge_id]

    def get_challenge_goal(self, challenge_id):
        """Savoir le but à atteindre selon son identifiant"""
        return self.__challenges_info[challenge_id]["goal"]

    def get_challenge_name(self, challenge_id):
        """Savoir le nom d'un défi en fonction de son identifiant"""
        return self.__challenges_info[challenge_id]["name"].replace("GOAL", str(self.get_challenge_goal(challenge_id)))

    def get_all_challenges_id(self):
        """Avoir tous les identifiants des défis"""
        return self.__challenges_info.keys()

    def have_completed_challenge(self, challenge_id):
        """Savoir si un défi a été complété selon son identifiant"""
        return self.get_challenge_goal(challenge_id) == self.get_challenge_state(challenge_id)

    def write_file(self):
        """Écrire ce qu'il y a en mémoire pour enregistrer les défis"""
        with open(self.__FILE_PATH, "w") as file:
            file.write(json.dumps(self.__challenges_user))
