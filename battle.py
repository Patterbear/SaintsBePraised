from tkinter import Tk, Frame, Label, Canvas, E, PhotoImage, Button, W

# Executes attackers chosen move
from tkinter.scrolledtext import ScrolledText

from game import font_large, font_medium


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


def battle(card_1, card_2):
    battle_screen = Tk()
    battle_screen.title("Saints Be Praised - Battle")

    # Setting
    background_image = PhotoImage(file="data/images/hell1.png")
    background_label = Label(battle_screen, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Card 2 (opponent) status widget
    card_2_status_frame = Frame(battle_screen)
    card_2_status_frame.grid(row=0, column=0)

    # Name and health labels
    Label(card_2_status_frame, text=card_2.name, font=font_large).grid(row=0, column=0, columnspan=3)

    # Health icon
    health_icon = PhotoImage(file="data/images/icon-health.png").subsample(50, 50)
    health_icon_label = Label(card_2_status_frame, image=health_icon)
    health_icon_label.image = health_icon
    health_icon_label.grid(row=1, column=0)

    #  Health bar
    card_2_healthbar = Canvas(card_2_status_frame, height=20)
    card_2_healthbar.config(background="White")
    card_2_healthbar.grid(row=1, column=1, columnspan=4)

    # Level label
    Label(card_2_status_frame, text="Level " + str(card_2.level), font=font_medium).grid(row=0, column=4, sticky=E)

    # Enemy sprite
    card_2_sprite = PhotoImage(file="data/images/" + card_2.card_id + "-sprite.png").subsample(3, 3)
    card_2_sprite_label = Label(battle_screen, image=card_2_sprite)
    card_2_sprite_label.image = card_2_sprite
    card_2_sprite_label.grid(row=0, column=2, columnspan=2, rowspan=3, sticky=E)

    # Player sprite
    card_1_sprite = PhotoImage(file="data/images/" + card_1.card_id + "-sprite.png").subsample(3, 3)
    card_1_sprite_label = Label(battle_screen, image=card_1_sprite)
    card_1_sprite_label.image = card_1_sprite
    card_1_sprite_label.grid(row=3, column=0, rowspan=3, sticky=W)

    # Card 1 status widget
    card_1_status_frame = Frame(battle_screen)
    card_1_status_frame.grid(row=5, column=1, columnspan=3)

    # Name and health labels
    Label(card_1_status_frame, text=card_1.name, font=font_large).grid(row=0, column=0, columnspan=3)

    # Health icon
    health_icon = PhotoImage(file="data/images/icon-health.png").subsample(50, 50)
    health_icon_label = Label(card_1_status_frame, image=health_icon)
    health_icon_label.image = health_icon
    health_icon_label.grid(row=1, column=0)

    #  Health bar
    card_1_healthbar = Canvas(card_1_status_frame, height=20)
    card_1_healthbar.config(background="White")
    card_1_healthbar.grid(row=1, column=1, columnspan=4)

    # Level label
    Label(card_1_status_frame, text="Level " + str(card_1.level), font=font_medium).grid(row=0, column=4, sticky=E)

    # Combat log
    combat_log = ScrolledText(battle_screen, width=40, height=5, font=font_medium)
    combat_log.grid(row=6, column=0)

    # Player buttons
    attack_button = Button(battle_screen, text="Attack", font=font_medium)
    attack_button.grid(row=6, column=1)
    defend_button = Button(battle_screen, text="Defend", font=font_medium)
    defend_button.grid(row=6, column=2)
    heal_button = Button(battle_screen, text="Heal", font=font_medium)
    heal_button.grid(row=6, column=3)



    battle_screen.mainloop()
