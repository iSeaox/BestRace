import os

__FILE_PATH = os.path.abspath(".") + "\data\\score.data"

def store_new_score(score):
    """Permet de stocker à la fin du fichier un nouveau score"""
    with open(__FILE_PATH, "a") as file:
        file.write(str(score)+"\n")

def get_scores():
    """Renvoie une liste des scores rangés par ordre décroissant"""
    scores = []
    with open(__FILE_PATH, "a+") as file:
        file.seek(0)
        for line in file.readlines():
            line = line.replace("\n", "")
            scores.append(int(line))
    scores.sort(reverse=True)
    return scores
