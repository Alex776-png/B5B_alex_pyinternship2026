class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]


inventory = Inventory()

inventory.add_item("Laptop")
inventory.add_item("Mouse")
inventory.add_item("Keyboard")

print(len(inventory))
print(inventory[1])