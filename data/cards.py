# Collection of Dictionaries defining the different classes
# these haven't been put in one dictionary because saints, knights and divines will have their own subclasses with unique attributes and methods

saints = {
    "saint-george": ["George of Lydda", "england", 50, 500, 70, 60, ["dragon-slayer", "unwavering-faith", "praetorian-guard"]],
    "saint-andrew": ["Andrew the Apostle", "scotland", 50, 500, 30, 50, ["apostle-of-christ", "fisher-of-men", "martyred-by-crucifixion"]],
    "saint-david": ["David of Mynyw", "wales", 50, 500, 20, 50, ["raising-the-earth", "asceticism", "vision-from-christ"]],
    "saint-patrick": ["Patrick the Enlightener", "ireland", 50, 500, 60, 50, ["snake-banisher", "fast-on-the-mountain", "enlightener-of-ireland"]],
    "saint-michael": ["Michael the Archangel", "all", 70, 750, 80, 60, []]
}

knights = {
    "knight-player": ["Knight", "nowhere", 5, 75, 15, 15, []],
    "knight-rival": ["Knight Rival", "nowhere", 5, 50, 10, 10, []],
    "knight-trainer": ["Knight Trainer", "nowhere", 5, 30, 10, 10, []],
    "knight-veteran": ["Knight Veteran", "nowhere", 8, 40, 15, 15, ["veteran-strike"]],
    "knight-of-england": ["Knight of England", "england", 10, 100, 25, 25, ["warrior-of-god", "for-nation", "healing-prayer"]],
    "knight-of-scotland": ["Knight of Scotland", "scotland", 10, 100, 25, 25, ["warrior-of-god", "for-nation", "healing-prayer"]],
    "knight-of-wales": ["Knight of Wales", "wales", 10, 100, 25, 25, ["warrior-of-god", "for-nation", "healing-prayer"]],
    "knight-of-ireland": ["Knight of Ireland", "ireland", 10, 100, 25, 25, ["warrior-of-god", "for-nation", "healing-prayer"]],
}

divines = {
    "almighty-god": ["The Almighty God", "all", 100, 100000, 100000, 100000, ["divine-wrath"]],
    "jesus-christ": ["The Lord Jesus Christ", "all", 100, 1000, 500, 500, ["son-of-god", "resurrection"]],
}

demons = {
    "demon-knight": ["Demon Knight", "demon", 10, 50, 10, 10, []],
    "demon-sorcerer": ["Demon Sorcerer", "demon", 10, 50, 10, 10, []],
    "demon-warlord": ["Demon Warlord", "demon", 30, 100, 30, 30, []],
}

horsemen = {
    "horseman-conquest": ["Conquest", "horseman", 50, 500, 80, 50, []],
    "horseman-war": ["War", "horseman", 50, 500, 90, 60, []],
    "horseman-famine": ["Famine", "horseman", 50, 500, 70, 80, []],
    "horseman-death": ["Death", "horseman", 50, 500, 100, 100, []],
}

# I know St. Michael is both. Multiple categories will be allowed
angels = {
    "angel-cherubim": ["Cherubim", "all", 40, 400, 60, 60,[]],
    #"angel-throne": ["Throne", "angel", 40, 400, 60, 60,[]],
}

# Temporary category
others = {
    "moses": ["Moses", "all", 80, 800, 90, 90, []],
}
