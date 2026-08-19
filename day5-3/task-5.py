class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if not self.__items:
            raise IndexError("Cannot pop from an empty stack.")
        return self.__items.pop()

    def __str__(self):
        return f"Stack({self.__items})"