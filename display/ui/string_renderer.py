import textures.ui.text as t_text

def render_string(text, space_size = 3):
    """Cette fonction permet de renvoyer l'affichage du string text
    exemple:
      ████    ████      ████    ██████
    ██    ██  ██  ██  ██    ██  ██    ██
    ██    ██  ████    ██        ██    ██
    ████████  ██  ██  ██    ██  ██    ██
    ██    ██  ██████    ████    ██████
    """
    char_height = 5
    space_btw_letter = 1

    text = text.replace(" ", " "*space_size)

    rendered = []
    for i in range(char_height):
        rendered.append("")

    for char in text:
        t_char = t_text.character[char]

        splited = t_char.split("\n")
        splited = splited[1:len(splited) - 1]

        char_width = 0
        for line in splited:
            if(len(line) // 2 > char_width):
                char_width = len(line) // 2

        for n_line in range(len(splited)):
            temp = ""
            for char in splited[n_line]:
                temp += char

            while(len(temp) < char_width * 2):
                temp += " "

            rendered[n_line] += temp + "  "

    to_return = ""
    for line in rendered:
        to_return += line + "\n"
    return to_return
