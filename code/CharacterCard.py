from Utilities import Collections, Effects


class CharacterCard:
    def __init__(self, name, picNumber: int, quotes: list, filename: str, effects: Effects = Effects.NONE,
                 aliases: str = "no aliases", collection: Collections = Collections.NONE):
        self.name = name
        self.picNumber = picNumber
        self.quotes = quotes
        self.filename = filename
        self.effects = effects
        self.aliases = aliases
        self.collection = collection


class ACharacterCard:
    def __init__(self, name, picNumber, quotes: list, footers: list, game: str):
        self.name = name
        self.picNumber = picNumber
        self.quotes = quotes
        self.footers = footers
        self.game = game
