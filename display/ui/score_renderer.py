import textures.ui.score as t_score


def render_score(score):
    score_width = 3
    score_height = 7
    space = 1
    tab_score = []
    for number in str(score):
        tab_score.append(int(number))
    print(tab_score)
