class ListOfList:
    def __init__(self) -> None:
        self.keys = []
        self.values = []

    def append(self, key, value):
        self.keys.append(key)
        self.values.append(value)

    def __getitem__(self, key):
        return self.values[self.keys.index(key)]

    def iter(self):
        raise NotImplementedError("Please use mylist.getkeys()")

    def remove(self, key):
        self.values.remove(
            self.keys.pop(self.keys.index(key)))

    def getkeys(self):
        return self.keys

    def getvalues(self):
        return self.values


mylist = ListOfList()
mylist.append("a", "ffz")
mylist.append(1, 5)
mylist.append("b", "fkfkf")
mylist.append(2, 6)

for i in mylist:
    print(i)
