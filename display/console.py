class Console:

    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.clear_canvas()


    def blit(self, textures, x, y):
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
        self.__canvas = []
        for line in range(self.height):
            temp = []
            for pos in range(self.width):
                temp.append(0)
            self.__canvas.append(temp)

    def render(self):
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
