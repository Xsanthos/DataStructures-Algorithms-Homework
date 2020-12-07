from Translator_Functions import *
import json


class Item:

    def __init__(self, name, price, weight, type):
        self.name = name
        self.price = float(price)
        self.weight = float(weight)
        self.type = type

    def getItemCost(self):
        return self.price

    def getItemWeight(self):
        return self.weight

    def getItemType(self):
        return self.type

    def getItemName(self):
        return self.name

    def displayInformation(self):
        print("Name: ", self.getItemName())
        print("Price: ", self.getItemCost(), "(gp)")
        print("Weight: ", self.getItemWeight(), "(lbs)")
        print("Type: ", self.getItemType())


class Character:

    def __init__(self, name, strength_score, amount_of_gold):
        self.name = name,
        self.strength = strength_score
        self.carryingCapacity = 10 * self.strength
        self.inventory = HashMap()
        self.encumbrance = float(self.carryingCapacity)
        self.coinPurse = float(amount_of_gold)

    def addItem(self, item):
        if self.encumbrance - item.getItemWeight() < 0:
            print("There is no space on your person for a/an/_  ", item.name)
            return
        self.encumbrance = self.encumbrance - item.getItemWeight()
        self.coinPurse = self.coinPurse - item.getItemCost()
        self.inventory.put(item.name, item)

    def removeItem(self, item):
        if self.inventory.hasKey(item) is False:
            print("It seems you have lost this item in your travels! It is not in you inventory")
            return
        self.encumbrance = self.encumbrance + item.getItemWeight()
        self.inventory.remove(item.name, item)
        self.coinPurse = self.coinPurse + item.getItemCost()

    def displayInventory(self):
        for e in self.inventory._hashtable:
            while e is not None:
                print(e.key, ":")
                e.value.displayInformation()
                break

    def getRemainingSpace(self):
        return self.encumbrance


class Shop:

    def __init__(self):
        self.storage = HashMap()

    def importShop(self, shop_name):
        with open(str(shop_name)+".json") as data:
            dictionary = json.load(data)
            self.storage = dict_to_hashmap(dictionary)

    def printStorage(self):
        self.storage.nested_print()

    def getSpecificInformation(self, item):
        item.displayInformation()



