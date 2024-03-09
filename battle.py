from tkinter import Tk, Frame, Label, Canvas, E, PhotoImage, Button, N, INSERT, END

# Executes attackers chosen move
from tkinter.scrolledtext import ScrolledText
from turtle import RawTurtle, TurtleScreen

from animations.combat import draw_battle, animate_attack, animate_heal, animate_brace
from data.moves import get_move

# Temporary to prevent circular imports
font_large = "Helvetica 20"
font_medium = "Helvetica 15"
font_small = "Helvetica 10"
font_extra_small = "Helvetica 8"


# Temporary to prevent circular imports
def screen_size(root):
    return [root.winfo_screenwidth(), root.winfo_screenheight()]


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


# Menu back function
# closes a menu and toggles main buttons back on
def menu_back(buttons, menu):
    menu.destroy()
    toggle_buttons(buttons, True)


# Toggle buttons function
# enables/disables main battle screen buttons
def toggle_buttons(buttons, on):
    if on:
        state = 'normal'
    else:
        state = 'disabled'

    for button in buttons:
        button.config(state=state)


# Moves menu
# brings up menu of player moves
def show_moves(battle_screen, buttons, card_1, x, y, choice_label):
    toggle_buttons(buttons, False)
    moves = Frame(battle_screen, background='')

    for i in range(0, len(card_1.moves)):
        move = card_1.moves[i]
        Button(moves, text=card_1.moves[i].title, font=font_medium, width=10, command=lambda this_move=move: choose_move(card_1, this_move, choice_label, moves, buttons)).pack()

    back_button = Button(moves, text='Back', font=font_medium, width=10, command=lambda: menu_back(buttons, moves))
    back_button.pack()

    moves.place(x=x, y=y - (40 * (len(card_1.moves) + 1)))


# Items menu
# brings up menu of player items
def show_items(battle_screen, buttons, card_1, x, y):
    items_demo = ["Manna", "Bread", "Fish"]
    toggle_buttons(buttons, False)
    items = Frame(battle_screen, background='')

    for i in range(0, len(items_demo)):
        Button(items, text=items_demo[i], font=font_medium, width=10).pack()

    back_button = Button(items, text='Back', font=font_medium, width=10, command=lambda: menu_back(buttons, items))
    back_button.pack()

    items.place(x=x, y=y - (40 * (len(items_demo) + 1)))


# Choose move function
# sets card's next move to the one chosen by the player and updates choice label
def choose_move(card, move, choice_label, menu, buttons):
    menu.destroy()
    card.next_move = move
    choice_label.config(text="Choice: " + move.title)
    toggle_buttons(buttons, True)


# Animate move function
# calls an animation function determined by the given move
def animate_move(canvas, card_1, card_2, battleground):
    print(card_1.next_move.move_id)
    match card_1.next_move.move_id:
        case "attack0":
            print("hello")
            animate_attack(canvas, card_1, card_2, battleground)
        case "heal0":
            animate_heal(canvas, card_1, card_2, battleground)
        case "brace0":
            animate_brace(canvas, card_1, card_2, battleground)


#  Advance function
# executes the player's chosen move and executes an enemy response
def advance(battle_canvas, card_1, card_2, healthbars, buttons, battleground, combat_log):
    # Disable buttons
    toggle_buttons(buttons, False)

    # Player card move

    # Combat log update
    combat_log.config(state='normal')
    combat_log.delete(1.0, END)
    combat_log.insert(INSERT, card_1.name + " uses " + card_1.next_move.title + ".")
    combat_log.config(state='disabled')

    # Animate move
    animate_move(battle_canvas, card_1, card_2, battleground)

    # Re-enable button
    toggle_buttons(buttons, True)


# Battle screen
def battle(card_1, card_2, battleground):
    battle_screen = Tk()
    battle_screen.title("Saints Be Praised - Battle")
    dimensions = screen_size(battle_screen)
    battle_screen.geometry(str(dimensions[0]) + "x" + str(dimensions[1]))

    # Begin coords for drawing on canvas, leaves equal spaces at sides
    canvas_begin = int((dimensions[0] - 1024) / 2)

    # Bottom canvas coords
    canvas_depth = 512

    # Canvas
    battle_canvas = Canvas(battle_screen, width=1024, height=canvas_depth)

    # Array for healthbars
    healthbars = []

    # Draw initial battle scene
    draw_battle(battle_canvas, card_1, card_2, battleground)

    # Card 1 status widget
    card_1_status_frame = Frame(battle_screen)

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
    healthbars.append(TurtleScreen(card_1_healthbar))
    draw_healthbar(healthbars[0], 100)

    # Level label
    Label(card_1_status_frame, text="Level " + str(card_1.level), font=font_medium).grid(row=0, column=4, sticky=E)

    # Place status frame
    card_1_status_frame.place(x=canvas_begin + 10, y=canvas_depth / 8)

    # Card 2 (opponent) status widget
    card_2_status_frame = Frame(battle_screen)

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
    healthbars.append(TurtleScreen(card_2_healthbar))
    draw_healthbar(healthbars[1], 100)

    # Level label
    Label(card_2_status_frame, text="Level " + str(card_2.level), font=font_medium).grid(row=0, column=4, sticky=E)

    # Place status frame
    card_2_status_frame.place(x=dimensions[0] - canvas_begin - 10 - card_2_status_frame.winfo_reqwidth(), y=canvas_depth / 8)

    battle_canvas.grid(row=0, column=0, columnspan=3, padx=(canvas_begin, 0))

    # Combat log
    combat_log = ScrolledText(battle_screen, width=51, height=5, font=font_medium, state='disabled')
    combat_log.grid(row=1, column=0, padx=(canvas_begin, 0), sticky=N)

    # Buttons panel
    buttons = Frame(battle_screen)
    buttons.grid(row=1, column=1, sticky=N)

    # Player buttons
    buttons_list = []
    moves_button = Button(buttons, text="Moves", font=font_large, width=6, command=lambda: show_moves(battle_screen, buttons_list, card_1, buttons.winfo_x(), buttons.winfo_y(), choice_label))
    moves_button.grid(row=0, column=0)
    items_button = Button(buttons, text="Items", font=font_large, width=6, command=lambda: show_items(battle_screen, buttons_list, card_1, buttons.winfo_x() + moves_button.winfo_width() + 5, buttons.winfo_y()))
    items_button.grid(row=0, column=1, padx=5)
    cards_button = Button(buttons, text="Cards", font=font_large, width=6, command=lambda: draw_battle(battle_canvas, card_1, card_2, battleground, [256, 0, 10, 0]))
    cards_button.grid(row=1, column=0, pady=5)
    options_button = Button(buttons, text="Options", font=font_large,  width=6, command=lambda: draw_battle(battle_canvas, card_1, card_2, battleground, [-10, 0, -256, 0]))
    options_button.grid(row=1, column=1, padx=5, pady=5)

    buttons_list = [moves_button, items_button, cards_button, options_button]

    # Frame to display player choice and advance button
    choice_frame = Frame(battle_screen)

    # Player choice label
    choice_label = Label(choice_frame, text="Choice: None", font=font_medium, width=16)
    choice_label.pack()

    # Advance button
    advance_icon = PhotoImage(master=choice_frame, file="data/images/icons/icon-advance.png").subsample(8, 9)
    advance_button = Button(choice_frame, image=advance_icon, command=lambda: advance(battle_canvas, card_1, card_2, healthbars, buttons_list, battleground, combat_log))
    advance_button.advance_icon = advance_icon
    advance_button.pack()

    buttons_list.append(advance_button)

    choice_frame.grid(row=1, column=2)

    battle_screen.mainloop()
