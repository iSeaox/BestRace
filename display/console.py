class Console:
    """Cette classe permet de gérer la console et l'affichage sur celle-ci"""
    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.clear_canvas()


    def blit(self, textures, x, y):
        """Dessine sur le canvas de la console la textures donnée en paramètre 
        aux coordonnées (x, y). Il est a noté que le (0, 0) se situe tout en haut à gauche 
        De plus, si la texture est partiellement ou entièrement en dehors des coordonnées
        admis, (de (0, 0) à (self.width - 1, self.height - 1)), la méthode ajoutera au 
        canvas uniquement les parties visibles"""

        t_splited = textures.split("\n")
        for i in range(len(t_splited)):
            j = 0
            while(j < len(t_splited[i])):
                if(t_splited[i][j:(j+2)] == "██"):
                    if((y + i) < self.height and (x + (j // 2)) < self.width):
                        self.__canvas[y + i][x + (j // 2)] = 1
                j += 2

    def get_canvas(self):
        return self.__canvas

    def clear_canvas(self):
        """Renvoie un nouveau canvas vide"""
        self.__canvas = []
        for line in range(self.height):
            temp = []
            for pos in range(self.width):
                temp.append(0)
            self.__canvas.append(temp)

    def render(self):
        """Renvoie une liste de string qui correspond aux lignes à 
        afficher dans la console python""" 
        temp = []
        for i in range(self.height):
            line = ""
            for k in range(self.width):
                if(self.__canvas[i][k]):
                    line += "██"
                else:
                    line += "  "
            temp.append(line + "\n")

        return temp
