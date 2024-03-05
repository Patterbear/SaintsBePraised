# Collection of Dictionaries defining the different classes
# these haven't been put in one dictionary because saints, knights and divines will have their own subclasses with unique attributes and methods

saints = {
    "saint-george": ["saint", "George of Lydda", "england", 50, 500, 70, 60, ["dragon-slayer", "unwavering-faith", "praetorian-guard"]],
    "saint-andrew": ["saint", "Andrew the Apostle", "scotland", 50, 500, 30, 50, ["apostle-of-christ", "fisher-of-men", "martyred-by-crucifixion"]],
    "saint-david": ["saint", "David of Mynyw", "wales", 50, 500, 20, 50, ["raising-the-earth", "asceticism", "vision-from-christ"]],
    "saint-patrick": ["saint", "Patrick the Enlightener", "ireland", 50, 500, 60, 50, ["snake-banisher", "fast-on-the-mountain", "enlightener-of-ireland"]],
    "saint-michael": ["saint", "Michael the Archangel", "heaven", 70, 750, 80, 60, []]
}

knights = {
    "knight-player": ["knight", "Knight", "nowhere", 5, 75, 15, 15, []],
    "knight-rival": ["knight", "Knight Rival", "nowhere", 5, 50, 10, 10, []],
    "knight-trainer": ["knight", "Knight Trainer", "nowhere", 5, 30, 10, 10, []],
    "knight-veteran": ["knight", "Knight Veteran", "nowhere", 8, 40, 15, 15, ["veteran-strike"]],
    "knight-of-england": ["knight", "Knight of England", "england", 10, 100, 25, 25, ["warrior-of-god", "for-nation", "healing-prayer"]],
    "knight-of-scotland": ["knight", "Knight of Scotland", "scotland", 10, 100, 25, 25, ["warrior-of-god", "for-nation", "healing-prayer"]],
    "knight-of-wales": ["knight", "Knight of Wales", "wales", 10, 100, 25, 25, ["warrior-of-god", "for-nation", "healing-prayer"]],
    "knight-of-ireland": ["knight", "Knight of Ireland", "ireland", 10, 100, 25, 25, ["warrior-of-god", "for-nation", "healing-prayer"]],
}

divines = {
    "almighty-god": ["divine", "Almighty God", "heaven", 100, 100000, 100000, 100000, ["divine-wrath"]],
    "jesus-christ": ["divine", "Lord Jesus Christ", "heaven", 100, 1000, 500, 500, ["son-of-god", "resurrection"]],
}

demons = {
    "demon-knight": ["demon", "Demon Knight", "hell", 10, 50, 10, 10, []],
    "demon-sorcerer": ["demon", "Demon Sorcerer", "hell", 10, 50, 10, 10, []],
    "demon-warlord": ["demon", "Demon Warlord", "hell", 30, 100, 30, 30, []],
}

horsemen = {
    "horseman-conquest": ["horseman", "Conquest", "apocalypse", 50, 500, 80, 50, []],
    "horseman-war": ["horseman", "War", "apocalypse", 50, 500, 90, 60, []],
    "horseman-famine": ["horseman", "Famine", "apocalypse", 50, 500, 70, 80, []],
    "horseman-death": ["horseman", "Death", "apocalypse", 50, 500, 100, 100, []],
}

# I know St. Michael is both. Multiple categories will be allowed
angels = {
    #"angel-cherubim": ["angel", "Cherubim", "heaven", 40, 400, 60, 60,[]],
    #"angel-throne": ["Throne", "angel", 40, 400, 60, 60,[]],
}

# Temporary category
others = {
    "moses": ["other", "Moses", "israel", 80, 800, 90, 90, []],
    "john-the-baptist": ["other", "John the Baptist", "heaven", 80, 800, 90, 90, []],
}
