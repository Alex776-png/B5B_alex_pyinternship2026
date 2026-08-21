class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if self.__items:
            return self.__items.pop()

    def __str__(self):
        return str(self.__items)


stack = Stack()

stack.push("A")
stack.push("B")
stack.push("C")

print(stack)
stack.pop()
print(stack)