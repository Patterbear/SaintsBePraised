import tkinter

from classes.card import Card
from data.cards import saints, knights, divines, demons

# Game fonts
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


# Load cards function
# loads all cards from storage into list for main game
def load_cards():
    loaded_cards = []

    # Append saint objects
    saints_list = create_cards_from_list(saints)
    for i in range(0, len(saints_list)):
        loaded_cards.append(saints_list[i])
        saints_list[i].get_ability(saints_list[i].abilities[0])

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

    return loaded_cards


# Display card screen
# visually displays 'card'
def display_card(master, card):
    profile = tkinter.Toplevel(master)
    profile.title(card.name)

    # Nation icon
    nation_icon = tkinter.PhotoImage(file="data/images/icon-" + card.nation + ".png").subsample(30, 30)
    nation_icon_label = tkinter.Label(profile, image=nation_icon)
    nation_icon_label.image = nation_icon
    nation_icon_label.grid(row=0, column=0)

    # Card name
    name_label = tkinter.Label(profile, text=card.name, font=font_medium)
    name_label.grid(row=0, column=1, columnspan=4)

    # Card level
    tkinter.Label(profile, text="Level: " + str(card.level), font=font_small).grid(row=0, column=5)

    # Card image
    card_image = tkinter.PhotoImage(file="data/images/" + card.card_id + ".png").subsample(3, 3)
    card_image_label = tkinter.Label(profile, image=card_image)
    card_image_label.image = card_image  # keep image in memory
    card_image_label.grid(row=1, column=0, columnspan=6)

    # Health stat
    health_icon = tkinter.PhotoImage(file="data/images/icon-health.png").subsample(30, 30)
    health_icon_label = tkinter.Label(profile, image=health_icon, font=font_small)
    health_icon_label.image = health_icon
    health_icon_label.grid(row=2, column=0)
    tkinter.Label(profile, text=str(card.health)).grid(row=2, column=1)

    # Attack stat
    attack_icon = tkinter.PhotoImage(file="data/images/icon-attack.png").subsample(30, 30)
    attack_icon_label = tkinter.Label(profile, image=attack_icon, font=font_small)
    attack_icon_label.image = attack_icon
    attack_icon_label.grid(row=2, column=2)
    tkinter.Label(profile, text=str(card.attack)).grid(row=2, column=3)

    # Defence stat
    defence_icon = tkinter.PhotoImage(file="data/images/icon-defence.png").subsample(30, 30)
    defence_icon_label = tkinter.Label(profile, image=defence_icon, font=font_small)
    defence_icon_label.image = defence_icon
    defence_icon_label.grid(row=2, column=4)
    tkinter.Label(profile, text=str(card.defence)).grid(row=2, column=5)

    # Abilities
    row = 3
    column = 0
    for i in range(0, len(card.abilities)):
        ability = card.get_ability(card.abilities[i])
        bullet_point = tkinter.PhotoImage(file="data/images/icon-all.png").subsample(40, 40)
        bullet_point_label = tkinter.Label(profile, image=bullet_point)
        bullet_point_label.grid(row=row, column=column)
        bullet_point_label.image = bullet_point
        tkinter.Label(profile, text=ability[0], font=font_medium).grid(row=row, column=column+1, columnspan=4)
        tkinter.Label(profile, text=ability[1], font=font_medium).grid(row=row, column=column+5)
        tkinter.Label(profile, text=ability[2], font=font_extra_small).grid(row=row+1, column=column, columnspan=6)
        row += 2


# Main function
def main():
    root = tkinter.Tk()
    root.winfo_toplevel().iconphoto(True, tkinter.Image("photo", file="data/images/icon-all.png"))
    root.title("Saints Be Praised - Demo")

    cards = load_cards()
    for i in range(0, len(cards)):
        display_card(root, cards[i])

    root.mainloop()


if __name__ == "__main__":
    main()
