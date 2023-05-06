import discord
from discord import Embed, File
from enum import Enum

class Collections(Enum):
    NONE = 0  # non-collectibles; embedded orange
    HAREM = 1  # kidnapped by Axel, saved by Orion; embedded pink
    SIDE_DISHES = 2  # kidnapped by TBD, saved by TBD; embedded purple
    THE_HOMIES = 3  # attacked by Thanatos, saved by Calypso; embedded yellow
    CREATURES = 4 # attacked by golem, saved by pyramid head

    def __str__(self):
        if self == Collections.NONE:
            return "No Collection"
        elif self == Collections.HAREM:
            return "Harem"
        elif self == Collections.SIDE_DISHES:
            return "Side Girls"
        elif self == Collections.THE_HOMIES:
            return "The Homies"
        elif self == Collections.CREATURES:
            return "Creatures"


class Effects(Enum):
    NONE = 0  # no effects; embedded orange
    HAREM_SAVIOUR = 1  # saves harem from Thanatos
    SIDE_GIRL_SAVIOUR = 2  # saves sides from Axel
    HOMIE_SAVIOUR = 3  # saves homies from troll
    HAREM_KILLER = 4  # kills a harem member
    SIDE_GIRL_KIDNAPPER = 5  # kidnaps a side girl
    HOMIE_KILLER = 6  # kills a homie
    CREATURE_SAVIOUR = 7  # saves a creature
    CREATURE_STOMPER = 8  # kills a creature



class HelperClass():
    orange = 0xffa800  # default
    eternumBlue = 0x00ffcc  # eternum default
    pink = 0xb502b8  # eternum harem
    purple = 0x530554  # eternum side girls
    red = 0xff0000  # eternum denied villain
    black = 0x000000  # eternum successful villain
    yellow = 0xeeff00  # eternum homies
    green = 0x57F287  # eternum creatures
    blue = 0x0028ff  # protectors

    async def createEmbed(self, title, text, color=orange, footer=None):
        embed = discord.Embed(title=title, description=text, colour=color)
        if footer is not None:
            embed.set_footer(text=footer)
        return embed

    daliaParty = "<:ChibiDaliaParty:1005859600400138391> "
    alexAngry = "<:ChibiAlexAngry:1001483487016132648>"
    annieCry = "<:ChibiAnnieCry:1001482701410422795>"
    annieYay = "<:ChibiAnnieYay:1001481596504920104>"
    novaGun = "<:ChibiNovaGun:1006135279087788072>"
    pepeCry2 = "<:PepeCry2:759731151312257075>"



