from random import choice


# Card class
class Card(object):
    def __init__(self, card_id, name, nation, level, health, power, defence, moves):
        self.card_id = card_id
        self.name = name
        self.nation = nation
        self.level = level
        self.max_health = health
        self.health = health
        self.power = power
        self.defence = defence
        self.moves = moves
        self.next_move = None

    # Random move choice
    def choose_random_move(self):
        self.next_move = choice(self.moves)

    # Informed move choice
    # more likely to heal or defend the lower health is
    def choose_move(self):
        self.next_move = choice(self.moves)

    # Attack function
    def attack(self, other_card):
        damage = (int((self.power * 0.25) + self.next_move.strength))
        defended = int(other_card.defence * 0.25)

        print(defended)

        # prevents too much defence causing healing
        if defended > damage:
            damage = self.next_move.strength
        other_card.health -= damage

        print(damage)

    # Defend function
    def defend(self):
        self.defence += self.next_move.strength

    # Heal function
    def heal(self):
        self.health += int(self.max_health * (self.next_move.strength * 0.01))

        # prevents overhealing
        if self.health > self.max_health:
            self.health = self.max_health

    def __str__(self):
        return self.card_id + ": [ Name: " + self.name + ", Nation: " + self.nation + ", Level: " + str(self.level) + ", Health: " + str(self.max_health) + ", Attack/Defence: " + str(self.power) + "/" + str(self.defence) + " ]"
