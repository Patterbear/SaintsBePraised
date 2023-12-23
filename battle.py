from data.abilities import moves


# Executes attackers chosen move
def execute_move(attacker, defender):
    move = moves.get(attacker.next_move)
    if move[0] == "attack":
        attacker.attack(defender)
    elif move[0] == "defence":
        attacker.defend()
    elif move[0] == "health":
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
            move = moves.get(card_1.next_move)
            print(card_1.name + " uses " + move[1])
            execute_move(card_1, card_2)
        else:
            card_2.choose_move()
            move = moves.get(card_2.next_move)
            print(card_2.name + " uses " + move[1])
            execute_move(card_2, card_1)

        if card_1.health < 1 or card_2.health < 1:
            print("Game over.")
            turns = 0

        turns -= 1

