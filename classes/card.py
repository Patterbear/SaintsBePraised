from random import choice, randint

from data.abilities import moves

# Card class
class Card(object):
    def __init__(self, card_id, name, nation, level, health, power, defence, abilities):
        self.card_id = card_id
        self.name = name
        self.nation = nation
        self.level = level
        self.max_health = health
        self.health = health
        self.power = power
        self.defence = defence
        self.abilities = abilities
        self.next_move = []

    def get_ability(self, move_id):
        ability = moves.get(move_id).copy()
        if move_id == "for-nation":
            ability[0] += self.nation.capitalize()
        return ability

    # Random move choice
    def choose_random_move(self):
        self.next_move = choice(self.abilities)

    # Informed move choice
    # more likely to heal or defend the lower health is
    def choose_move(self):
        health_percentage = int((self.health / self.max_health) * 100)
        if randint(0, 100) < health_percentage:
            self.next_move = "attack0"
        else:
            self.next_move = choice(["brace0", "heal0"])

    # Attack function
    def attack(self, other_card):
        damage = (int((self.power * 0.5) + moves.get(self.next_move)[5]))
        defended = int(other_card.defence * 0.25)

        # prevents too much defence causing healing
        if defended > damage:
            damage = 0
        else:
            damage = damage - defended
        other_card.health -= damage

    # Defend function
    def defend(self):
        self.defence += moves.get(self.next_move)[5]

    # Heal function
    def heal(self):
        self.health += int(self.max_health * (moves.get(self.next_move)[5] * 0.01))

        # prevents overhealing
        if self.health > self.max_health:
            self.health = self.max_health

    def __str__(self):
        return self.card_id + ": [ Name: " + self.name + ", Nation: " + self.nation + ", Level: " + str(self.level) + ", Health: " + str(self.health) + ", Attack/Defence: " + str(self.power) + "/" + str(self.defence) + " ]"
