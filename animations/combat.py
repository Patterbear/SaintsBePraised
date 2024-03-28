from time import sleep
from tkinter import PhotoImage, NW


# Get sprite width function
def get_sprite_width(card):
    sprite = PhotoImage(file="data/images/sprites/" + card.card_id + "-sprite.png")

    # Divided by 2 as sprites are usually sub sampled by 2 anyway
    return sprite.width() / 2


# Get sprite height function
def get_sprite_height(card):
    sprite = PhotoImage(file="data/images/sprites/" + card.card_id + "-sprite.png")

    # Divided by 2 as sprites are usually sub sampled by 2 anyway
    return sprite.height() / 2


# Draw battle scene function
# draws sprites, battleground and effects to canvas
# can be used to animate sprites and display effects
def draw_battle(canvas, card_1, card_2, battleground, offsets=None):
    if offsets is None:
        offsets = [0, 0, 0, 0]

    canvas.delete('all')

    # Background
    background_image = PhotoImage(master=canvas, file="data/images/backgrounds/" + battleground + ".png").subsample(1, 2)
    canvas.create_image(0, 0, image=background_image, anchor=NW)
    canvas.background_image = background_image

    # Player sprite
    player_sprite = PhotoImage(master=canvas, file="data/images/sprites/" + card_1.card_id + "-sprite.png").subsample(2,
                                                                                                                      2)
    canvas.create_image(10 + (player_sprite.width() / 2) + offsets[0], 512 - (player_sprite.height() / 2) + offsets[1], image=player_sprite)
    canvas.player_sprite = player_sprite

    # Opponent sprite
    opponent_sprite = PhotoImage(master=canvas, file="data/images/sprites/" + card_2.card_id + "-sprite-reverse.png").subsample(2, 2)
    canvas.create_image(1014 - (opponent_sprite.width() / 2) + offsets[2], 512 - (opponent_sprite.height() / 2) + offsets[3], image=opponent_sprite)
    canvas.opponent_sprite = opponent_sprite

    canvas.update()


# Display effect function
# displays given effect at given coordinates
def display_effect(canvas, x, y, effect):
    effect_image = PhotoImage(master=canvas, file="data/images/effects/" + effect + ".png").subsample(3, 3)
    canvas.create_image(x, y, image=effect_image)
    canvas.effect_image = effect_image

    canvas.update()


# Attack animation
def animate_attack(canvas, attacker, defender, battleground, player):
    if player:
        coords = [[-15, 0, 0,0], [384, 0, 0, 0], [0, 0, -15, 0], [0, 0, 15, 0]]
        effect_x = 834
        effect = "attack"
    else:
        coords = [[0, 0, 15, 0], [0, 0, -384, 0], [-15, 0, -0, 0], [15, 0, 0, 0]]
        effect_x = 190
        effect = "attack-reverse"

    draw_battle(canvas, attacker, defender, battleground, coords[0])
    sleep(1)
    draw_battle(canvas, attacker, defender, battleground, coords[1])
    display_effect(canvas, effect_x, canvas.winfo_reqheight() / 2, effect)
    sleep(1)
    draw_battle(canvas, attacker, defender, battleground, coords[2])
    sleep(1)
    draw_battle(canvas, attacker, defender, battleground, coords[3])
    sleep(1)
    draw_battle(canvas, attacker, defender, battleground)


# Heal animation
def animate_heal(canvas, healer, opponent, battleground, player):
    draw_battle(canvas, healer, opponent, battleground, [0, 10, 0, 0])
    sleep(1)
    display_effect(canvas, (get_sprite_width(healer) / 2) + 10, canvas.winfo_reqheight() / 2, "prayer")
    sleep(1)
    draw_battle(canvas, healer, opponent, battleground)


# Brace animation
def animate_brace(canvas, defender, opponent, battleground, player):
    draw_battle(canvas, defender, opponent, battleground, [-15, 0, 0, 0])
    sleep(1)
    display_effect(canvas, (get_sprite_width(defender) / 2) - 5, (canvas.winfo_reqheight() / 2) + (get_sprite_height(defender) / 4), "brace")
    sleep(1)
    draw_battle(canvas, defender, opponent, battleground)
