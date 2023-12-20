import tkinter

from classes.card import Card
from data.cards import saints, knights, divines

# Game fonts
font_large = "Helvetica 20"
font_medium = "Helvetica 10"


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

    return loaded_cards


# Display card screen
# visually displays 'card'
def display_card(master, card):
    profile = tkinter.Toplevel(master)
    profile.title(card.name)

    # Nation icon
    nation_icon = tkinter.PhotoImage(file="data/images/" + card.nation + "-icon.png").subsample(20, 20)
    nation_icon_label = tkinter.Label(profile, image=nation_icon)
    nation_icon_label.image = nation_icon
    nation_icon_label.grid(row=0, column=0)

    # Card name
    name_label = tkinter.Label(profile, text=card.name, font=font_large)
    name_label.grid(row=0, column=1, columnspan=2)

    # Card image
    card_image = tkinter.PhotoImage(file="data/images/" + card.card_id + ".png").subsample(4, 4)
    card_image_label = tkinter.Label(profile, image=card_image)
    card_image_label.image = card_image  # keep image in memory
    card_image_label.grid(row=1, column=1, columnspan=5)


# Main function
def main():
    root = tkinter.Tk()
    root.title("Saints Be Praised - Demo")

    cards = load_cards()
    for i in range(0, len(cards)):
        display_card(root, cards[i])

    root.mainloop()


if __name__ == "__main__":
    main()
