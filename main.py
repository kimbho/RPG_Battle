from classes.game import BColors, Person
from classes.magic import Spell
from classes.inventory import Item

# Create white magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Fire", 10, 100, "black")
blizzard = Spell("Fire", 10, 100, "black")
meteor = Spell("Fire", 20, 200, "black")
quake = Spell("Fire", 14, 140, "black")

# Create white magic
cure = Spell("Cure", 12, 120, "white")
ayur = Spell("Ayur", 18, 200, "white")

# Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hiPotions = Item("Hi -Potion", "potion", "Heals 100 HP", 100)
superPotion = Item("Super-Potion", "potion", "Heals 500 HP", 500)
elixir = Item("Elixir", "elixir", "Fully restore HP / MP of one parity member", 9999)
hiElixir = Item("MegaElixir", "elixir", "Fully rstores party's HP / MP", 9999)

grenade = Item("Grenade", "atatck", "Deals 500 Damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, ayur]
player_items = [potion, hiPotions, superPotion, elixir, hiElixir, grenade]

# Instantiate players
player = Person(460, 65, 60, 34, player_spells, player_items)
enemy = Person(1200, 65, 45, 25, [], [])

running = True
i = 0

print(BColors.FAIL + BColors.BOLD + "AN ENEMY ATTACK" + BColors.ENDC)

while running:
    print("=================================")
    player.choose_actions()
    choice = input("Choose action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for ", dmg, " points of damage. ")

    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic: ")) - 1

        if item_choice == -1:
            continue

        # magic_damage = player.generate_spell_damage(magic_choice)
        # spell = player.get_spell_name(magic_choice)
        # cost = player.get_spell_mp_cost(magic_choice)

        spell = player.magic[magic_choice]
        magic_damage = player.magic[magic_choice].generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(BColors.FAIL + "\nNot Enough MP\n" + BColors.ENDC)
            continue

        if spell.type == "white":
            player.heal(magic_damage)
            print(BColors.OKBLUE + "\n" + spell.name + " heals for", str(magic_damage), "HP." + BColors.ENDC)

        if spell.type == "black":
            enemy.take_damage(magic_damage)
            print(BColors.OKBLUE + "\n" + spell.name + " heals for ", str(magic_damage), "HP." + BColors.ENDC)

        player.reduce_mp(spell.cost)

    elif index == 2:
        player.choose_item()
        item_choice = int(input("Choose item: ")) - 1

        if item_choice == -1:
            continue

        item = player.items[item_choice]

        if item.type == "potion":
            player.heal(item.prop)
            print(BColors.OKGREEN + "\n" + item.name + " heals for ", str(item.prop), "HP", BColors.ENDC)

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg)

    print("=============================")
    print("Enemy HP:", BColors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + BColors.ENDC + "\n")

    print("Your HP:", BColors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + BColors.ENDC + "\n")
    print("Your MP:", BColors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + BColors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(BColors.OKGREEN + "You Win !" + BColors.ENDC);
        running = False
    elif player.get_hp() == 0:
        print(BColors.FAIL + "Your enemy has defeated you !" + BColors.ENDC);
        running = False
