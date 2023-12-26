# format: type, title, cost, description, duration, strength
from classes.move import Move

moves = {
    "attack0": ["attack", "Attack", 10, "Deal 5 damage.",0, 5],
    "attack1": ["attack", "Improved Attack", 10,  "Deal 10 damage.",0, 10],
    "attack2": ["attack", "Advanced Attack", 10, "Deal 15 damage.", 0, 15],
    "attack3": ["attack", "Master Attack", 10, "Deal 20 damage.", 0, 20],
    "divine-wrath": ["attack", "Divine Wrath", 0,  "Destroy enemy.", 0, 100000],
    "brace0": ["defence", "Brace", 10, "Reduce incoming damage by 5.", 0, 5],
    "brace1": ["defence", "Improved Brace", 10, "Reduce incoming damage by 10.", 0, 10],
    "brace2": ["defence", "Advanced Brace", 10, "Reduce incoming damage by 15.", 0, 15],
    "brace3": ["defence", "Master Brace", 10, "Reduce incoming damage by 20.", 0, 20],
    "protection-of-god": ["defence", "Protection of God.", 60, "Take no damage from the next attack.", 0, 100000],
    "heal0": ["health", "Prayer", 40, "Heal 5% health.", 0, 5],
    "heal1": ["health", "Improved Prayer", 40, "Heal 10% health.", 0, 10],
    "heal2": ["health", "Advanced Prayer", 40, "Heal 15% health.", 0, 15],
    "heal3": ["health", "Master Prayer", 40, "Heal 20% health.", 0, 20],
}


# Produces a move object from move ID
def get_move(move_id):
    move = moves.get(move_id)
    return Move(move_id, move[0], move[1], move[2], move[3], move[4], move[5])

"""
"dragon-slayer": ["Dragon Slayer", 80, "Attack increases by 30 and enemy defence is ignored.", 0, 30, 0, ["attack-increase," "ignore-defence"], 50],
"unwavering-faith": ["Unwavering Faith", 20,  "Defence increase of 20 for 2 turns.", 0, 0, 20, ["increase-defence"], 2],
"praetorian-guard": ["Praetorian Guard", 50, "Increase attack and defense by 15 for 3 turns.", 0, 15, 15, ["increase-attack", "increase-defence"], 3],
"apostle-of-christ": ["Apostle of Christ", 40, "Increase defence by 20 and heal 10 points per turn for 3 turns.", 10, 0, 20, ["increase-defence", "healing"], 3],
"fisher-of-men": ["Fisher of Men", 60, "Increase attack by 10 for 4 turns.", 0, 10, 0, "increase-attack", 3],
"martyred-by-crucifixion": ["Martyred by Crucifixion", 80, "Defence increases by 40 and health by 30.", 30, 0, 40, ["increase-defence", "healing"], 50],
"raising-the-earth": ["Raising the Earth", 40, "Attack increases by 20 for 2 turns.", 0, 20, 0, ["increase-attack"], 2],
"asceticism": ["Asceticism", 20, "Increase defence by 10 for 2 turns.", 0, 0, 10, ["increase-defence"], 2],
"vision-from-christ": ["Vision from Christ",  60, "Heal 30 points.", 10, 0, 0, ["healing"], 1],
"snake-banisher": ["Snake Banisher", 80, "Attack increases by 40.", 0, 40, 0, ["increase-attack"], 50],
"fast-on-the-mountain": ["Fast on the Mountain", 40, "Increase health and defence by 10 for 2 turns.", 10, 0, 10, ["healing", "increase-defence"], 2],
"enlightener-of-ireland": ["Enlightener of Ireland", 30, "Increase attack by 10 for 2 turns.", 0, 10, 0, ["increase-attack"], 2],
"warrior-of-god": ["Warrior of God", 20,  "Increase defence by  20 for 2 turns.", 0, 0, 20, ["increase-defence"], 2],
"for-nation": ["For ", 20, "Increase attack by 20 for 2 turns.", 0, 20, 0, ["increase-attack"], 2],
"healing-prayer": ["Healing Prayer", 40, "Heal 20 points.", 20, 0, 0, ["healing"], 1],
"son-of-god": ["Son of God", 30, "Increase attack and defence by 50", 0, 50, 50, ["increase-attack", "increase-defence"], 1],
"resurrection": ["Resurrection", 60, "Heal 100 points.", 100, 0, 0, ["healing"], 1],
"""