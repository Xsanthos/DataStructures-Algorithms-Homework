import json

invulnerable_vagrant = {}
invulnerable_vagrant["crystal"] = {"name": "Crystal", "price": "10", "weight": "1", "type": "focus"}
invulnerable_vagrant["orb"] = {"name": "Orb", "price": "20", "weight": "3", "type": "focus"}
invulnerable_vagrant["rod"] = {"name": "Rod", "price": "10", "weight": "2", "type": "focus"}
invulnerable_vagrant["staff"] = {"name": "Staff", "price": "5", "weight": "4", "type": "focus"}
invulnerable_vagrant["wand"] = {"name": "Wand", "price": "10", "weight": "1", "type": "focus"}

gilmores_glorious_goods = {}
gilmores_glorious_goods["spring"] = {"name": "Spring_of_Mistletoe", "price": "1", "weight": "0", "type": "focus"}
gilmores_glorious_goods["totem"] = {"name": "Totem", "price": "1", "weight": "0", "type": "focus"}
gilmores_glorious_goods["wooden_staff"] = {"name": "Wooden_Staff", "price": "5", "weight": "4", "type": "focus"}
gilmores_glorious_goods["yew_wand"] = {"name": "Yew_Wand", "price": "10", "weight": "1", "type": "focus"}
gilmores_glorious_goods["amulet"] = {"name": "Amulet", "price": "5", "weight": "1", "type": "holy_symbol"}
gilmores_glorious_goods["emblem"] = {"name": "Emblem", "price": "5", "weight": "0", "type": "holy_symbol"}
gilmores_glorious_goods["reliquary"] = {"name": "Reliquary", "price": "5", "weight": "2", "type": "holy_symbol"}

general_shop = {}
general_shop["abacus"] = {"name": "Abacus", "price": "2", "weight": "2", "type": "tool"}
general_shop["acid"] = {"name": "Acid_(vial)", "price": "25", "weight": "1", "type": "concoction"}
general_shop["alch_fire"] = {"name": "Alchemist_Fire_(flask)", "price": "50", "weight": "1", "type": "concoction"}
general_shop["arrows"] = {"name": "Arrows_20", "price": "1", "weight": "1", "type": "ammunition"}
general_shop["needles"] = {"name": "Blowgun_Needles_50", "price": "1", "weight": "1", "type": "ammunition"}
general_shop["bolts"] = {"name": "Crossbow_Bolts_20", "price": "1", "weight": "1.5", "type": "ammunition"}
general_shop["bullets"] = {"name": "Sling_Bullets_20", "price": "0.04", "weight": "1.5", "type": "ammunition"}
general_shop["antitoxin"] = {"name": "Antitoxin", "price": "50", "weight": "0", "type": "concoction"}
general_shop["backpack"] = {"name": "Backpack", "price": "2", "weight": "5", "type": "container"}
general_shop["ball_bearings"] = {"name": "Ball_Bearings_1000", "price": "1", "weight": "2", "type": "random_item"}
general_shop["barrel"] = {"name": "Barrel", "price": "2", "weight": "70", "type": "container"}
general_shop["basket"] = {"name": "Basket", "price": "0.4", "weight": "2", "type": "container"}
general_shop["bedroll"] = {"name": "Bedroll", "price": "1", "weight": "7", "type": "cloth"}
general_shop["bell"] = {"name": "Bell", "price": "1", "weight": "0", "type": "random_item"}
general_shop["blanket"] = {"name": "Blanket", "price": "0.5", "weight": "3", "type": "cloth"}
general_shop["block_tackle"] = {"name": "Block_and_Tackle", "price": "1", "weight": "5", "type": "random_item"}
general_shop["book"] = {"name": "Book", "price": "25", "weight": "5", "type": "random_item"}
general_shop["bottle"] = {"name": "Glass_Bottle", "price": "2", "weight": "2", "type": "container"}
general_shop["bucket"] = {"name": "Bucket", "price": "0.05", "weight": "2", "type": "container"}
general_shop["caltrops"] = {"name": "Caltrops_20", "price": "1", "weight": "2", "type": "random_itme"}
general_shop["candle"] = {"name": "Candle", "price": "0.01", "weight": "0", "type": "light"}
general_shop["case_bolts"] = {"name": "Crossbow_Bolt_Case", "price": "1", "weight": "1", "type": "container"}
general_shop["case_scroll"] = {"name": "Map_Scroll_Case", "price": "1", "weight": "1", "type": "container"}
general_shop["chain"] = {"name": "Chain_10_feet", "price": "5", "weight": "10", "type": "random_item"}
general_shop["chalk"] = {"name": "Chalk_1", "price": "0.01", "weight": "0", "type": "random_item"}
general_shop["chest"] = {"name": "Chest", "price": "5", "weight": "25", "type": "container"}
general_shop["climbers_kit"] = {"name": "Climbers_Kit", "price": "12", "weight": "", "type": "gear"}
general_shop["clothes_common"] = {"name": "Common_Clothes", "price": "0.5", "weight": "3", "type": "clothing"}
general_shop["clothes_common"] = {"name": "Costume_Clothes", "price": "5", "weight": "4", "type": "clothing"}
general_shop["clothes_common"] = {"name": "Fine_Clothes", "price": "15", "weight": "6", "type": "clothing"}
general_shop["clothes_common"] = {"name": "Traveler_Clothes", "price": "2", "weight": "4", "type": "clothing"}
general_shop["component_pouch"] = {"name": "Component_Pouch", "price": "25", "weight": "", "type": "focus"}
general_shop["crowbar"] = {"name": "Crowbar", "price": "2", "weight": "", "type": "tool"}
general_shop["fishing_tackle"] = {"name": "Fishing_Tackle", "price": "1", "weight": "", "type": "tool"}
general_shop["flask_tankard"] = {"name": "Flask_or_Tankard", "price": "0.02", "weight": "", "type": "container"}
general_shop["grappling_hook"] = {"name": "Grappling_Hook", "price": "2", "weight": "", "type": "tool"}
general_shop["hammer"] = {"name": "Hammer", "price": "", "weight": "1", "type": "tool"}
general_shop["sledgehammer"] = {"name": "Sledgehammer", "price": "2", "weight": "3", "type": "tool"}
general_shop["healers_kit"] = {"name": "Healers_Kit", "price": "5", "weight": "10", "type": "tool"}


with open("./invulnerable_vagrant.json", "w") as file:
    json.dump(invulnerable_vagrant, file, sort_keys=True, indent=2)

with open("./gilmores_glorious_goods.json", "w") as file:
    json.dump(gilmores_glorious_goods, file, sort_keys=True, indent=2)

with open("./general_shop.json", "w") as file:
    json.dump(general_shop, file, sort_keys=True, indent=2)