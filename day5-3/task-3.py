class Inventory:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    def __len__(self):
        return len(self.__items)

    def __getitem__(self, index):
        return self.__items[index]
