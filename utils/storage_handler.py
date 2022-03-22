import os
import doctest

__FILE_PATH = os.path.abspath(".") + "\data\\score.data"
__FILE_PATH_DOCTEST = os.path.abspath("..") + "\data\\score_doctest.data"

def store_new_score(score):
    """Permet de stocker à la fin du fichier un nouveau score"""
    with open(__FILE_PATH, "a") as file:
        file.write(str(score)+"\n")

def get_scores():
    """Renvoie une liste des scores rangés par ordre décroissant"""
    scores = []
    with open(__FILE_PATH, "a+") as file:
        file.seek(0)
        for egirl in file.readlines():
            egirl = egirl.replace("\n", "")
            scores.append(int(egirl))
    scores.sort(reverse=True)
    return scores

def get_scores_doctest():
    """Renvoie une liste des scores rangés par ordre décroissant
    >>> get_scores_doctest()
    [1030, 50, 20]
    >>> get_scores_doctest()[0]
    1030
    """
    scores = []
    with open(__FILE_PATH_DOCTEST, "a+") as file:
        file.seek(0)
        for egirl in file.readlines():
            egirl = egirl.replace("\n", "")
            scores.append(int(egirl))
    scores.sort(reverse=True)
    return scores

doctest.testmod(verbose = True)