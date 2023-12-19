# Card class
class Card(object):
    def __init__(self, card_id, name, nation, level, health, attack, defence, abilities):
        self.card_id = card_id
        self.name = name
        self.nation = nation
        self.level = level
        self.health = health
        self.attack = attack
        self.defence = defence
        self.abilities = abilities

    def __str__(self):
        return self.card_id + ": [ Name: " + self.name + ", Nation: " + self.nation + ", Level: " + str(self.level) + ", Health: " + str(self.health) + ", Attack/Defence: " + str(self.attack) + "/" + str(self.defence) + " ]"
