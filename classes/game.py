import random
from .magic import Spell
import pprint


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.hp = hp
        self.maxhp = hp
        self.mp = mp
        self.maxmp = mp
        self.atk = atk
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic", "Items"]
        self.items = items
        self.name = name

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_spell_damage(self, i):
        mgl = self.magic[i]["damage"] - 5
        mgh = self.magic[i]["damage"] + 5
        return random.randrange(mgl, mgh)

    def take_damage(self, dmg):
        self.hp = self.hp - dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    # def get_spell_name(self, i):
    #     return self.magic[i]["name"]
    #
    # def get_spell_mp_cost(self, i):
    #     return self.magic[i]["cost"]

    def choose_actions(self):
        i = 1
        print(BColors.BOLD + "    " + self.name + BColors.BOLD + BColors.ENDC)
        print(BColors.BOLD + BColors.OKBLUE + "    Actions" + BColors.BOLD + BColors.ENDC)
        for item in self.actions:
            print("        " + str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + BColors.OKBLUE + BColors.BOLD + "    Magic" + BColors.ENDC)
        for spell in self.magic:
            print("        ", str(i), ":", spell.name, str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + BColors.OKGREEN + BColors.BOLD + "    ITEMS: " + BColors.ENDC)
        for item in self.items:
            print("        ", str(i) + ".", item["item"].name, ":", item["item"].desc, "(x " + str(item["quantity"]) + ")")
            i+=1

    def get_stats(self):
        print("                  _________________________            __________")
        print(BColors.BOLD + self.name + ":    "
              + str(self.hp) + '/' + str(self.mp) + " " + BColors.OKGREEN + "|████████████████|"
              + BColors.ENDC + BColors.BOLD + "    " + str(self.mp) + '/' + str(self.maxmp) + " "
              + BColors.OKBLUE + BColors.BOLD + "|██████|" + BColors.ENDC + BColors.BOLD)