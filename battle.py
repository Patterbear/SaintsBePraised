from data.moves import moves


# Executes attackers chosen move
def execute_move(attacker, defender):
    move = attacker.next_move
    if move.category == "attack":
        attacker.attack(defender)
    elif move.category == "defence":
        attacker.defend()
    elif move.category == "health":
        attacker.heal()
    else:
        return


# Auto battle functions
# runs a text based battle
def auto_battle(card_1, card_2):
    turns = 100

    while turns > 0:
        print("================================= Turn " + str(101 - turns ) + " ===========================================")
        print(card_1.name + " has " + str(card_1.health) + " health.")
        print(card_2.name + " has " + str(card_2.health) + " health.")
        if turns % 2 == 0:
            card_1.choose_move()
            print(card_1.name + " uses " + card_1.next_move.title)
            execute_move(card_1, card_2)
        else:
            card_2.choose_move()
            print(card_2.name + " uses " + card_2.next_move.title)
            execute_move(card_2, card_1)

        if card_1.health < 1 or card_2.health < 1:
            print("Game over.")
            turns = 0

        turns -= 1


def battle(root, card_1, card_2):
    return