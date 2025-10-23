class ShoppingList:
    def __init__(self):
        self.shopping_list = []

    def add_item(self, item):
        self.shopping_list.append(item.lower())
        print(item)

    def get_num_items(self):
        print(len(self.shopping_list))

    def get_list_items(self):
        print(self.shopping_list)

    def remove_item(self,item):
        self.shopping_list.remove(item)
        print(self.shopping_list)



class ShoppingItem(ShoppingList):
    def __init__(self, item_name, item_quantity):
        self.item_name = item_name
        self.item_quantity = item_quantity

    def get_item_name(self):
        return self.item_name

    def set_item_quantity(self, item_quantity):
        self.item_quantity = item_quantity

    def get_item_quantity(self):
        return self.item_quantity



steves_list = ShoppingList()
item1 = ShoppingItem("Milk", 1)
item2 = ShoppingItem("Eggs", 6)

print(item1.item_name)
print(item2.item_quantity)
item2.item_quantity = 12
print(item2.item_quantity)
print(steves_list.add_item(item1))
print(steves_list.get_num_items)