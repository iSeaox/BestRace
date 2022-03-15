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

    def pop(self, index):
        item = self.values.pop(index)
        self.keys.pop(index)
        return item

    def getkeys(self):
        return self.keys

    def getvalues(self):
        return self.values

    def __len__(self):
        return len(self.keys)
