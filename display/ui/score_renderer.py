import textures.ui.score as t_score

def render_score(score):
    score_width = 3
    score_height = 5
    space = 1
    tab_score = []

    rendered = []
    for i in range(score_height):
        rendered.append("")

    for number in str(score):
        tab_score.append(int(number))
        num = t_score.numbers[int(number)]
        splited = num.split("\n")
        splited = splited[1:len(splited) - 1]
        for n_line in range(len(splited)):
            temp = ""
            for char in splited[n_line]:
                temp += char

            while(len(temp) < score_width * 2):
                temp += " "

            rendered[n_line] += temp + "  "

    to_return = ""
    for line in rendered:
        to_return += line + "\n"
    return to_return
