from tkinter import Tk, Frame, Label, Canvas, E, PhotoImage, Button, NW

# Executes attackers chosen move
from tkinter.scrolledtext import ScrolledText
from turtle import RawTurtle, TurtleScreen

from data.moves import get_move

# Temporary to prevent circular imports
font_large = "Helvetica 20"
font_medium = "Helvetica 15"
font_small = "Helvetica 10"
font_extra_small = "Helvetica 8"


# Temporary to prevent circular imports
def screen_size(root):
    return str(root.winfo_screenwidth()) + "x" + str(root.winfo_screenheight())


# Attack function
# calls the attacking card's 'attack' function on the defending card
# updates the defender's health bar
def attack(attacker, defender, healthbar):
    attacker.next_move = get_move("attack0")
    attacker.attack(defender)
    draw_healthbar(healthbar, int((defender.health / defender.max_health) * 100))


# Heal function
# calls the healer card's 'heal' function
# updates the healer's health bar
def heal(healer, healthbar):
    healer.next_move = get_move("heal0")
    healer.heal()
    draw_healthbar(healthbar, int((healer.health / healer.max_health) * 100))


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
    healthbar.tracer(0, 0)
    turtle = RawTurtle(healthbar)
    turtle.hideturtle()
    turtle.width(15)
    turtle.penup()


    # Fill health bar
    turtle.goto(-150, 0)
    turtle.color('red')
    turtle.pendown()
    turtle.forward(300)

    # Remove health
    turtle.color('white')
    turtle.back(300 * ((100 - percentage) * 0.01))

    healthbar.update()


def battle(card_1, card_2, battleground):
    battle_screen = Tk()
    battle_screen.title("Saints Be Praised - Battle")
    battle_screen.geometry(screen_size(battle_screen))

    # Canvas
    canvas = Canvas(battle_screen, width=1024, height=1024)

    # Background image
    background_image = PhotoImage(master=canvas, file="data/images/backgrounds/" + battleground + ".png")
    canvas.create_image(10, 10, image=background_image, anchor=NW)
    canvas.background_image = background_image

    # Player sprite
    player_sprite = PhotoImage(master=canvas, file="data/images/sprites/" + card_1.card_id + "-sprite.png").subsample(2, 2)
    canvas.create_image(210, 475, image=player_sprite)
    canvas.player_sprite = player_sprite

    # Card 1 status widget
    card_1_status_frame = Frame(battle_screen)
    card_1_status_frame.place(x=170, y=225)

    # Name and health labels
    Label(card_1_status_frame, text=card_1.name, font=font_large).grid(row=0, column=0, columnspan=3)

    # Health icon
    health_icon = PhotoImage(master=card_1_status_frame, file="data/images/icons/icon-health.png").subsample(50, 50)
    health_icon_label = Label(card_1_status_frame, image=health_icon)
    health_icon_label.image = health_icon
    health_icon_label.grid(row=1, column=0)

    #  Health bar
    card_1_healthbar = Canvas(card_1_status_frame, height=20, width=300)
    card_1_healthbar.grid(row=1, column=1, columnspan=4)
    card_1_healthbar_ts = TurtleScreen(card_1_healthbar)
    draw_healthbar(card_1_healthbar_ts, 100)

    # Level label
    Label(card_1_status_frame, text="Level " + str(card_1.level), font=font_medium).grid(row=0, column=4, sticky=E)

    # Opponent sprite
    opponent_sprite = PhotoImage(master=canvas, file="data/images/sprites/" + card_2.card_id + "-sprite-reverse.png").subsample(2, 2)
    canvas.create_image(830, 275, image=opponent_sprite)
    canvas.opponent_sprite = opponent_sprite

    # Card 2 (opponent) status widget
    card_2_status_frame = Frame(battle_screen)
    card_2_status_frame.place(x=790, y=20)

    # Name and health labels
    Label(card_2_status_frame, text=card_2.name, font=font_large).grid(row=0, column=0, columnspan=3)

    # Health icon
    health_icon = PhotoImage(master=card_2_status_frame, file="data/images/icons/icon-health.png").subsample(50, 50)
    health_icon_label = Label(card_2_status_frame, image=health_icon)
    health_icon_label.image = health_icon
    health_icon_label.grid(row=1, column=0)

    #  Health bar
    card_2_healthbar = Canvas(card_2_status_frame, height=20, width=300)
    card_2_healthbar.grid(row=1, column=1, columnspan=4)
    card_2_healthbar_ts = TurtleScreen(card_2_healthbar)
    draw_healthbar(card_2_healthbar_ts, 100)

    # Level label
    Label(card_2_status_frame, text="Level " + str(card_2.level), font=font_medium).grid(row=0, column=4, sticky=E)

    # Combat log
    combat_log = ScrolledText(battle_screen, width=30, height=6, font=font_medium)
    combat_log.place(x=460, y=475)

    # Player buttons
    attack_button = Button(battle_screen, text="Attack", font=font_large, command=lambda: attack(card_1, card_2, card_2_healthbar_ts))
    attack_button.place(x=850, y=475)
    defend_button = Button(battle_screen, text="Defend", font=font_large)
    defend_button.place(x=970, y=475)
    heal_button = Button(battle_screen, text="Heal", font=font_large, command=lambda: heal(card_2, card_2_healthbar_ts))
    heal_button.place(x=920, y=575)

    canvas.pack()

    battle_screen.mainloop()
