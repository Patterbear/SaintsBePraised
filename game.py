from os.path import exists
from random import choice
from tkinter import Tk, Label, Button, Toplevel, PhotoImage, Image

import battle
from classes.card import Card
from data.cards import saints, knights, divines, demons, horsemen, angels, others

# Game fonts
from data.moves import get_move

font_large = "Helvetica 20"
font_medium = "Helvetica 15"
font_small = "Helvetica 10"
font_extra_small = "Helvetica 8"


# Create card objects from list function
# creates a list of 'Card' objects based on data extracted from 'cards.py'
def create_cards_from_list(card_list):
    created_cards = []

    card_list_keys = list(card_list.keys())
    for i in range(0, len(card_list)):
        card_raw = card_list.get(card_list_keys[i])
        created_cards.append(
            Card(card_list_keys[i], card_raw[0], card_raw[1], card_raw[2], card_raw[3], card_raw[4], card_raw[5],
                 card_raw[6]))

    return created_cards


# Testing function to give all cards the basic moves
def set_moves_to_basic(cards):
    for i in range(0, len(cards)):
        cards[i].moves = [get_move("attack0"), get_move("brace0"), get_move("heal0")]

    return cards


# Load cards function
# loads all cards from storage into list for main game
def load_cards():
    loaded_cards = []

    # Append saint objects
    saints_list = create_cards_from_list(saints)
    for i in range(0, len(saints_list)):
        loaded_cards.append(saints_list[i])

    # Append knight objects
    knights_list = create_cards_from_list(knights)
    for i in range(0, len(knights_list)):
        loaded_cards.append(knights_list[i])

    # Append divine objects
    divines_list = create_cards_from_list(divines)
    for i in range(0, len(divines_list)):
        loaded_cards.append(divines_list[i])

    # Append demon objects
    demons_list = create_cards_from_list(demons)
    for i in range(0, len(demons_list)):
        loaded_cards.append(demons_list[i])

    # Append horsemen objects
    horsemen_list = create_cards_from_list(horsemen)
    for i in range(0, len(horsemen_list)):
        loaded_cards.append(horsemen_list[i])

    angels_list = create_cards_from_list(angels)
    for i in range(0, len(angels_list)):
        loaded_cards.append(angels_list[i])

    # Append other objects
    others_list = create_cards_from_list(others)
    for i in range(0, len(others_list)):
        loaded_cards.append(others_list[i])

    # Set all card moves to the basic ones
    loaded_cards = set_moves_to_basic(loaded_cards)

    return loaded_cards


# Display card screen
# visually displays 'card'
def display_card(master, card):
    profile = Toplevel(master)
    profile.title(card.name)

    # Nation icon
    nation_icon = PhotoImage(file="data/images/icon-" + card.nation + ".png").subsample(30, 30)
    nation_icon_label = Label(profile, image=nation_icon)
    nation_icon_label.image = nation_icon
    nation_icon_label.grid(row=0, column=0)

    # Card name
    name_label = Label(profile, text=card.name, font=font_medium)
    name_label.grid(row=0, column=1, columnspan=4)

    # Card level
    Label(profile, text="Level: " + str(card.level), font=font_small).grid(row=0, column=5)

    # Card image
    card_image = PhotoImage(file="data/images/" + card.card_id + ".png").subsample(3, 3)
    card_image_label = Label(profile, image=card_image)
    card_image_label.image = card_image  # keep image in memory
    card_image_label.grid(row=1, column=0, columnspan=6)

    # Health stat
    health_icon = PhotoImage(file="data/images/icon-health.png").subsample(30, 30)
    health_icon_label = Label(profile, image=health_icon, font=font_small)
    health_icon_label.image = health_icon
    health_icon_label.grid(row=2, column=0)
    Label(profile, text=str(card.health)).grid(row=2, column=1)

    # Attack stat
    attack_icon = PhotoImage(file="data/images/icon-attack.png").subsample(30, 30)
    attack_icon_label = Label(profile, image=attack_icon, font=font_small)
    attack_icon_label.image = attack_icon
    attack_icon_label.grid(row=2, column=2)
    Label(profile, text=str(card.power)).grid(row=2, column=3)

    # Defence stat
    defence_icon = PhotoImage(file="data/images/icon-defence.png").subsample(30, 30)
    defence_icon_label = Label(profile, image=defence_icon, font=font_small)
    defence_icon_label.image = defence_icon
    defence_icon_label.grid(row=2, column=4)
    Label(profile, text=str(card.defence)).grid(row=2, column=5)

    # Moves
    row = 3
    column = 0
    for i in range(0, len(card.moves)):

        bullet_point = PhotoImage(file="data/images/icon-" + card.moves[i].category + ".png").subsample(40, 40)
        bullet_point_label = Label(profile, image=bullet_point)
        bullet_point_label.grid(row=row, column=column)
        bullet_point_label.image = bullet_point
        Label(profile, text=card.moves[i].title, font=font_medium).grid(row=row, column=column+1, columnspan=4)
        Label(profile, text=card.moves[i].cost, font=font_medium).grid(row=row, column=column+5)
        Label(profile, text=card.moves[i].description, font=font_extra_small).grid(row=row+1, column=column, columnspan=6)
        row += 2


# Card catalogue
# displays all existing card titles and images
# allows the user to view the full cards by pressing the buttons underneath the images
def card_catalogue(master, cards):
    catalogue = Toplevel(master)
    catalogue.title("SaintsBePraised - Card Catalogue")

    row = 0
    column = 0
    for i in range(0, len(cards)):
        if column == 0:
            #Separator(catalogue, orient=HORIZONTAL).grid(row=row, column=column, columnspan=6, sticky=EW)
            row += 1
        card = cards[i]

        # Name
        Label(catalogue, text=card.name, font=font_medium).grid(row=row, column=column, padx=(5, 5))

        # Card image
        card_image = PhotoImage(file="data/images/" + card.card_id + ".png").subsample(12, 12)
        card_image_label = Label(catalogue, image=card_image)
        card_image_label.image = card_image  # keep image in memory
        card_image_label.grid(row=row+1, column=column)

        # View button
        Button(catalogue, text="View", font=font_small, command=lambda this_card=card: display_card(catalogue, this_card)).grid(row=row+2, column=column, pady=(2, 5))

        if column == 6:
            column = 0
            row = row + 3
        else:
            column += 1


# Random battle
# sets up an auto battle between to randomly selected cards
def random_battle(master, cards):
    master.destroy()

    card1 = choice(cards)
    card2 = choice(cards)
    battle.battle(card1, card2)

# Sprite test screen
# displays all sprites
def sprite_test(master, cards):
    sprites = Toplevel(master)
    sprites.title("SaintsBePraised - Sprite Test")

    column = 0
    row = 0

    for i in range(0, len(cards)):
        if exists("data/images/sprites/" + cards[i].card_id + "-sprite.png"):
            image = PhotoImage(file="data/images/sprites/" + cards[i].card_id + "-sprite.png").subsample(5, 5)
            image_label = Label(sprites, image=image)
            image_label.image = image  # keep image in memory
            image_label.grid(row=row, column=column)

            if column == 6:
                column = 0
                row += 1
            else:
                column += 1


# Main function
def main():
    root = Tk()
    root.winfo_toplevel().iconphoto(True, Image("photo", file="data/images/icon-all.png"))
    root.geometry("500x450")
    root.title("Saints Be Praised - Demo")

    # Load cards from file
    cards = load_cards()

    # Title image
    title_image = PhotoImage(file="data/images/titles.png").subsample(8, 8)
    title_image_label = Label(root, image=title_image)
    title_image_label.image = title_image  # keep image in memory
    title_image_label.pack()

    # Buttons
    Button(root, text="Card Catalogue", font=font_medium, command=lambda: card_catalogue(root, cards)).pack()
    Button(root, text="Random Battle", font=font_medium, command=lambda: random_battle(root, cards)).pack()
    Button(root, text="Sprite Test", font=font_medium, command=lambda: sprite_test(root, cards)).pack()


    root.mainloop()


if __name__ == "__main__":
    main()
