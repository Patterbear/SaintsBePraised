from random import randint
from tkinter import Tk, Label, Canvas, PhotoImage, NW, Button

# Temporary to prevent circular imports
font_large = "Helvetica 20"
font_medium = "Helvetica 15"
font_small = "Helvetica 10"
font_extra_small = "Helvetica 8"


card_1 = None
card_2 = None
player_type = 0
player_number = 0
opponent_type = 0
opponent_number = 0
cards = {}


# Divide cards by type function
# returns a dictionary of cards divided by type
def divide_by_type(all_cards):
    types = {}

    for card in all_cards:
        if card.type not in types.keys():
            types[card.type] = []
        types.get(card.type).append(card)

    return types


# Update sprite and background
def update_card_preview(card, canvas, player):

    canvas.delete('all')
    background_image = PhotoImage(file="data/images/backgrounds/" + card.nation + ".png").subsample(3, 3)
    canvas.create_image(10, 10, image=background_image, anchor=NW)
    canvas.background_image = background_image

    # Inverts sprites for opponent
    if player:
        sprite_path = "data/images/sprites/" + card.card_id + "-sprite.png"
    else:
        sprite_path = "data/images/sprites/" + card.card_id + "-sprite-reverse.png"

    sprite = PhotoImage(file=sprite_path).subsample(3, 3)
    canvas.create_image(170, 221, image=sprite)
    canvas.sprite = sprite


# Card class change function
# facilitates browsing through cards of a type
def card_change(canvas, name_label, player, forward):
    global player_number, opponent_number, player_type, opponent_type

    # Change player card
    if player is True:
        if forward is True:
            # If current card is the last one, goes back to the first
            if player_number == len(cards.get(list(cards.keys())[player_type])) - 1:
                player_number = 0
            else:
                player_number += 1
        else:
            # If current card is the first one, wraps around to last
            if player_number == 0:
                player_number = len(cards.get(list(cards.keys())[player_type])) - 1
            else:
                player_number -= 1
        card = cards.get(list(cards.keys())[player_type])[player_number]

    # Change opponent card
    else:
        if forward is True:
            # If current card is the last one, goes back to the first
            if opponent_number == len(cards.get(list(cards.keys())[opponent_type])) - 1:
                opponent_number = 0
            else:
                opponent_number += 1
        else:
            # If current card is the first one, wraps around to last
            if opponent_number == 0:
                opponent_number = len(cards.get(list(cards.keys())[opponent_type])) - 1
            else:
                opponent_number -= 1
        card = cards.get(list(cards.keys())[opponent_type])[opponent_number]

    update_card_preview(card, canvas, player)

    # Update label
    name_label.config(text=card.name)


# Card class change function
# facilitates browsing through classes
def card_class_change(canvas, class_label, name_label, player, forward):

    global cards, player_type, player_number, opponent_type, opponent_number

    # Change player class
    if player is True:
        if forward is True:
            # If current class is the last one, goes back to the first
            if player_type == len(list(cards.keys())) - 1:
                player_type = 0
            else:
                player_type += 1
        else:
            # If current class is the first one, wraps around to last
            if player_type == 0:
                player_type = len(list(cards.keys())) - 1
            else:
                player_type -= 1
        player_number = 0
        card = cards.get(list(cards.keys())[player_type])[player_number]

    # Change opponent class
    else:
        if forward is True:
            # If current class is the last one, goes back to the first
            if opponent_type == len(list(cards.keys())) - 1:
                opponent_type = 0
            else:
                opponent_type += 1
        else:
            # If current class is the first one, wraps around to last
            if opponent_type == 0:
                opponent_type = len(list(cards.keys())) - 1
            else:
                opponent_type -= 1
        opponent_number = 0
        card = cards.get(list(cards.keys())[opponent_type])[opponent_number]

    update_card_preview(card, canvas, player)

    # Update labels
    class_label.config(text=card.type.capitalize())
    name_label.config(text=card.name)


# Battle selection screen
# allows player to choose cards to fight
def battle_select(master, all_cards):
    master.destroy()
    global cards
    cards = divide_by_type(all_cards)
    types = list(cards.keys())

    global player_type, player_number, opponent_type, opponent_number, card_1, card_2
    player_type = randint(0, len(types) - 1)
    opponent_type = randint(0, len(types) - 1)

    player_number = randint(0, len(cards.get(types[player_type])) - 1)
    opponent_number = randint(0, len(cards.get(types[opponent_type])) - 1)

    card_1 = cards.get(list(cards.keys())[player_type])[player_number]
    card_2 = cards.get(list(cards.keys())[opponent_type])[opponent_number]

    battle_selection = Tk()
    battle_selection.title("Saints Be Praised - Battle Selection")
    battle_selection.geometry("925x475")

    # Title
    Label(battle_selection, text="Select Battle", font=font_large).grid(row=0, column=4, columnspan=5)

    # Card sprites with backgrounds
    player_canvas = Canvas(battle_selection, width=341, height=341)
    player_background_image = PhotoImage(file="data/images/backgrounds/" + card_1.nation + ".png").subsample(3, 3)
    player_canvas.create_image(10, 10, image=player_background_image, anchor=NW)
    player_canvas.background_image = player_background_image
    player_canvas.grid(row=3, column=1, columnspan=3)

    player_sprite = PhotoImage(file="data/images/sprites/" + card_1.card_id + "-sprite.png").subsample(3, 3)
    player_canvas.create_image(170, 221, image=player_sprite)
    player_canvas.player_sprite = player_sprite

    opponent_canvas = Canvas(battle_selection, width=341, height=341)
    opponent_background_image = PhotoImage(file="data/images/backgrounds/" + card_2.nation + ".png").subsample(3, 3)
    opponent_canvas.create_image(10, 10, image=opponent_background_image, anchor=NW)
    opponent_canvas.background_image = opponent_background_image
    opponent_canvas.grid(row=3, column=9, columnspan=3)

    opponent_sprite = PhotoImage(file="data/images/sprites/" + card_2.card_id + "-sprite-reverse.png").subsample(3, 3)
    opponent_canvas.create_image(170, 221, image=opponent_sprite)
    opponent_canvas.opponent_sprite = opponent_sprite

    # Class selectors
    player_class = Label(battle_selection, text=card_1.type.capitalize(), font=font_medium)
    player_class.grid(row=1, column=2)
    player_class_back = Button(battle_selection, text="<", font=font_small, command=lambda: card_class_change(player_canvas, player_class, player_card, True, False))
    player_class_back.grid(row=1, column=1)
    player_class_forward = Button(battle_selection, text=">", font=font_small, command=lambda: card_class_change(player_canvas, player_class, player_card, True, True))
    player_class_forward.grid(row=1, column=3)

    opponent_class_back = Button(battle_selection, text="<", font=font_small, command=lambda: card_class_change(opponent_canvas, opponent_class, opponent_card, False, False))
    opponent_class_back.grid(row=1, column=9)
    opponent_class = Label(battle_selection, text=card_2.type.capitalize(), font=font_medium)
    opponent_class.grid(row=1, column=10)
    opponent_class_forward = Button(battle_selection, text=">", font=font_small, command=lambda: card_class_change(opponent_canvas, opponent_class, opponent_card, False, True))
    opponent_class_forward.grid(row=1, column=11)

    # Card selectors
    player_card_back = Button(battle_selection, text="<", font=font_medium, command=lambda: card_change(player_canvas, player_card, True, False))
    player_card_back.grid(row=2, column=0)
    player_card = Label(battle_selection, text=card_1.name, font=font_medium)
    player_card.grid(row=2, column=1, columnspan=3)
    player_card_forward = Button(battle_selection, text=">", font=font_medium, command=lambda: card_change(player_canvas, player_card, True, True))
    player_card_forward.grid(row=2, column=4)

    opponent_card_back = Button(battle_selection, text="<", font=font_medium, command=lambda: card_change(opponent_canvas, opponent_card, False, False))
    opponent_card_back.grid(row=2, column=8)
    opponent_card = Label(battle_selection, text=card_2.name, font=font_medium)
    opponent_card.grid(row=2, column=9, columnspan=3)
    opponent_card_forward = Button(battle_selection, text=">", font=font_medium, command=lambda: card_change(opponent_canvas, opponent_card, False, True))
    opponent_card_forward.grid(row=2, column=12)

    battle_selection.mainloop()
    