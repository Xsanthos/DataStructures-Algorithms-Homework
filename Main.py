from Inventory_Tracker_classes import *


def Main():
    print("~~~~~~~ Welcome to the Inventory Tracker! ~~~~~~~")
    print("\n")
    print("Please create your character")
    print("\n")

    character_name = input("What is your name?: ")
    character_strength = input("On a scale of 1-20 how strong are you?: ")
    character_wealth = input("How many gold coins do you have?: ")

    character = Character(character_name, character_strength, character_wealth)
    shop_choice = Shop()

    while True:

        print("Which store do you want to go to?: ")
        print("Write 1 to go to the General Goods shop")
        print("Write 2 to go to Gilmores Glorious Goods shop")
        print("Write 3 to go to the Invulnerable Vagrant shop")
        choice = input("Input your choice: ")

        l = {"1": "general_shop", "2": "gilmores_glorious_goods", "3": "invulnerable_vagrant"}
        for item in l.keys():
            if item == choice:
                shop_choice.importShop(l[item])

        print("Welcome to our shop!")
        print("Here is what we have available ~~~~~")
        shop_choice.printStorage()
        amount_of_items_you_wish_to_buy = int(input("How many items are you looking to buy from this store?: "))
        for i in range(amount_of_items_you_wish_to_buy):
            chosen_item = str(input("Please choose the item you wish to buy(case and spelling sensitive): "))

            print("\n")
            item_value = shop_choice.storage.get(chosen_item)
            bought_item = Item(item_value.get("name"), item_value.get("price"), item_value.get("weight"), item_value.get("type"))
            character.addItem(bought_item)

        statement = input("Do you want to continue your shopping?(y/n)")
        if statement == "n":
            break
    character.displayInventoryProperties()
    print()
    character.displayInventoryList()
    print("Thank you for using the Inventory tracker! Safe travels adventurer!!.")


Main()
