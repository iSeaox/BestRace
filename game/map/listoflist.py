class ListOfList:
    def __init__(self) -> None:
        """Create a dict-like of python but it respect the order of the last added element"""
        self.__keys = []
        self.__values = []

    def append(self, key, value):
        self.__keys.append(key)
        self.__values.append(value)

    def __getitem__(self, key):
        return self.__values[self.__keys.index(key)]

    def iter(self):
        raise NotImplementedError("Please use mylist.getkeys()")

    def remove(self, key):
        self.__values.remove(
            self.__keys.pop(self.__keys.index(key)))

    def pop(self, index):
        item = self.__values.pop(index)
        self.__keys.pop(index)
        return item

    def get_keys(self):
        return self.__keys

    def get_values(self):
        return self.__values

    def __len__(self):
        return len(self.__keys)
