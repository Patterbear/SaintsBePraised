from tkinter import Tk, Frame, Label, Canvas, E, PhotoImage, Button, NW

# Executes attackers chosen move
from tkinter.scrolledtext import ScrolledText
from turtle import RawTurtle
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
        print("================================= Turn " + str(101 - turns) + " ===========================================")
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


# Update healthbar function
def draw_healthbar(healthbar, percentage):
    healthbar.delete('all')
    turtle = RawTurtle(healthbar)
    turtle.penup()
    turtle.goto(-150, 0)
    turtle.color('red')
    turtle.width(15)
    turtle.pendown()
    turtle.forward((percentage * 0.01) * 300)


def battle(card_1, card_2):
    battle_screen = Tk()
    battle_screen.title("Saints Be Praised - Battle")

    # Canvas
    canvas = Canvas(battle_screen, width=1024, height=1024)

    # Background image
    background_image = PhotoImage(file="data/images/hell1.png")
    canvas.create_image(10, 10, image=background_image, anchor=NW)
    canvas.background_image = background_image

    # Player sprite
    player_sprite = PhotoImage(file="data/images/sprites/" + card_1.card_id + "-sprite.png").subsample(2, 2)
    canvas.create_image(210, 475, image=player_sprite)
    canvas.player_sprite = player_sprite

    # Card 1 status widget
    card_1_status_frame = Frame(battle_screen)
    card_1_status_frame.place(x=20, y=225)

    # Name and health labels
    Label(card_1_status_frame, text=card_1.name, font=font_large).grid(row=0, column=0, columnspan=3)

    # Health icon
    health_icon = PhotoImage(file="data/images/icon-health.png").subsample(50, 50)
    health_icon_label = Label(card_1_status_frame, image=health_icon)
    health_icon_label.image = health_icon
    health_icon_label.grid(row=1, column=0)

    #  Health bar
    card_1_healthbar = Canvas(card_1_status_frame, height=20, width=300)
    card_1_healthbar.config(background="White")
    card_1_healthbar.grid(row=1, column=1, columnspan=4)
    draw_healthbar(card_1_healthbar, 100)

    # Level label
    Label(card_1_status_frame, text="Level " + str(card_1.level), font=font_medium).grid(row=0, column=4, sticky=E)

    # Opponent sprite
    opponent_sprite = PhotoImage(file="data/images/sprites/" + card_2.card_id + "-sprite-reverse.png").subsample(2, 2)
    canvas.create_image(830, 275, image=opponent_sprite)
    canvas.opponent_sprite = opponent_sprite

    # Card 2 (opponent) status widget
    card_2_status_frame = Frame(battle_screen)
    card_2_status_frame.place(x=610, y=20)

    # Name and health labels
    Label(card_2_status_frame, text=card_2.name, font=font_large).grid(row=0, column=0, columnspan=3)

    # Health icon
    health_icon = PhotoImage(file="data/images/icon-health.png").subsample(50, 50)
    health_icon_label = Label(card_2_status_frame, image=health_icon)
    health_icon_label.image = health_icon
    health_icon_label.grid(row=1, column=0)

    #  Health bar
    card_2_healthbar = Canvas(card_2_status_frame, height=20, width=300)
    card_2_healthbar.config(background="White")
    card_2_healthbar.grid(row=1, column=1, columnspan=4)
    draw_healthbar(card_2_healthbar, 50)

    # Level label
    Label(card_2_status_frame, text="Level " + str(card_2.level), font=font_medium).grid(row=0, column=4, sticky=E)

    # Combat log
    combat_log = ScrolledText(battle_screen, width=30, height=6, font=font_medium)
    combat_log.place(x=400, y=475)

    # Player buttons
    attack_button = Button(battle_screen, text="Attack", font=font_large)
    attack_button.place(x=790, y=475)
    defend_button = Button(battle_screen, text="Defend", font=font_large)
    defend_button.place(x=910, y=475)
    heal_button = Button(battle_screen, text="Heal", font=font_large)
    heal_button.place(x=860, y=575)

    canvas.pack()

    battle_screen.mainloop()
