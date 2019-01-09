import random

from classes.game import BColors, Person
from classes.inventory import Item
from classes.magic import Spell

# Header text
print("\n\n")
print("NAME               HP                                   MP")
print("                   _________________________            __________")

# Create attacks
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create white magic
cure = Spell("Cure", 12, 120, "white")
ayur = Spell("Ayur", 18, 200, "white")

# Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hiPotion = Item("Hi -Potion", "potion", "Heals 100 HP", 100)
superPotion = Item("Super-Potion", "potion", "Heals 500 HP", 500)
elixir = Item("Elixir", "elixir", "Fully restore HP / MP of one parity member", 9999)
hiElixir = Item("MegaElixir", "elixir", "Fully rstores party's HP / MP", 9999)

# Create a grenade item
grenade = Item("Grenade", "atatck", "Deals 500 Damage", 500)

# Create a list of spells and items to be used by player
player_spells = [fire, thunder, blizzard, meteor, cure, ayur]
player_items = [{"item": potion, "quantity": 15}, {"item": hiPotion, "quantity": 5},
                {"item": superPotion, "quantity": 5},
                {"item": elixir, "quantity": 5}, {"item": hiElixir, "quantity": 5}, {"item": grenade, "quantity": 5}]

# Instantiate players
player1 = Person("Valos", 460, 65, 60, 34, player_spells, player_items)
player2 = Person("Nickk", 460, 65, 60, 34, player_spells, player_items)
player3 = Person("Robot", 460, 65, 60, 34, player_spells, player_items)
enemy = Person("Magns", 1200, 65, 45, 25, [], [])

# Create a list of players
players = [player1, player2, player3]
running = True
i = 0

# UI stuff start here
print(BColors.FAIL + BColors.BOLD + "AN ENEMY ATTACK" + BColors.ENDC)

# while Loop true till you win or the enemy defeats you
while running:
    print("=================================")
    print("\n\n")
    print("Name :          HP: _____________________        MP: _________")
    for player in players:
        player.get_stats()

    print("\n")

    # Prints enemy status
    enemy.get_enemy_stats()

    # Player's turn to attack
    for player in players:
        player.choose_actions()
        choice = input("    Choose action: ")
        index = int(choice) - 1

        # Normal attack
        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print("You attacked for ", dmg, " points of damage. ")

        # Magic spell attack
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose magic: ")) - 1

            # Press -1 to choose again
            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_damage = player.magic[magic_choice].generate_damage()

            current_mp = player.get_mp()

            # Checks if you have enough balance
            if spell.cost > current_mp:
                print(BColors.FAIL + "\nNot Enough MP\n" + BColors.ENDC)
                continue

            # Check the type of attack
            if spell.type == "white":
                player.heal(magic_damage)
                print(BColors.OKBLUE + "\n" + spell.name + " heals for", str(magic_damage), "HP." + BColors.ENDC)

            if spell.type == "black":
                enemy.take_damage(magic_damage)
                print(BColors.OKBLUE + "\n" + spell.name + " heals for ", str(magic_damage), "HP." + BColors.ENDC)

            # Deduce used Magic Points
            player.reduce_mp(spell.cost)

        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose item: ")) - 1

            if item_choice == -1:
                continue

            # Check if the item is available for use
            item = player.items[item_choice]
            if player.items[item_choice]["quantity"] <= 0:
                print(BColors.FAIL + "\n" + "None left..." + BColors.ENDC)
            player.items[item_choice]["quantity"] -= 1

            # Potion and Elixir heals your Health points
            if item["item"].type == "potion":
                player.heal(item["item"].prop)
                print(BColors.OKGREEN + "\n" + item["item"].name + " heals for ", str(item["item"].prop), "HP",
                      BColors.ENDC)
                player.heal(item["item"].prop)
            elif item["item"].type == "elixir":
                if item.name == 'MegaElixir':
                    for i in player:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                    else:
                        player.hp = player.maxhp
                        player.mp = player.maxmp
                        player.hp = player.maxhp
                        player.mp = player.maxmp
                print(BColors.OKGREEN + "\n" + item["item"].name + " fully restores HP/MP" + BColors.ENDC)

            # Special attack weapons
            elif item["item"].type == "attack":
                enemy.take_damage(item["item"].prop)
                print(BColors.FAIL + "\n" + item["item"].name + " deals", str(item["item"].prop),
                      "points of damage" + BColors.ENDC)

    # Enemy's turn
    enemy_choice = 1
    # Randomly attacks one of the players
    target = random.randrange(0, 3)
    enemy_dmg = enemy.generate_damage()

    players[target].take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg)

    print("=============================")
    print("Enemy HP:", BColors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + BColors.ENDC + "\n")

    # Check for Enemy's health
    if enemy.get_hp() == 0:
        print(BColors.OKGREEN + "You Win !" + BColors.ENDC);
        running = False
    # Check for your health
    elif player.get_hp() == 0:
        print(BColors.FAIL + "Your enemy has defeated you !" + BColors.ENDC);
        running = False
