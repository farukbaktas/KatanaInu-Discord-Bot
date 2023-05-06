import discord
from discord import Embed, File
from discord.ext import commands, tasks
from discord.ext.commands import cooldown, BucketType
import random
from Utilities import HelperClass
from CharacterCard import ACharacterCard
import os

def find_image_extension(folder, filename_prefix):
    for ext in ['png', 'jpg', 'jpeg', 'gif']:
        if os.path.isfile(f"{folder}/{filename_prefix}.{ext}"):
            return ext
    return None

class KatanaInu(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Quotes for all Katana characters!
    All = ACharacterCard(name="KatanaInu Character Card",
                             picNumber=5,
                             quotes=["Join the unique KatanaInu universe", "Join the unique KatanaInu universe"],
                             footers=["KatanaInu Battle Royale Game", "KatanaInu Battle Royale Game"],
                             game="KatanaInu")

    options = []
    options.append(All)

    katanainu = []
    katanainu.append(All)


    @commands.command()
    async def katanainu(self, ctx, parameter=None):

        choice = ""
        if parameter is None:
            choice = random.choice(self.options)
        elif parameter.lower() == "all":
            choice = self.All

        elif parameter.lower() == "katanainu":
            choice = random.choice(self.katanainu)

        else:
            choice = random.choice(self.options)

        color = HelperClass.orange
        if choice.game == "KatanaInu":
            color = HelperClass.eternumBlue

        embed = discord.Embed(title=choice.name, description=random.choice(choice.quotes), colour=color)
        embed.set_footer(text=random.choice(choice.footers))
        number = random.randint(1, choice.picNumber)
        image_ext = find_image_extension(f'./Pics/{choice.game}/{choice.name}', f'{choice.name}_{number}')

        if image_ext:
            image = discord.File(f'./Pics/{choice.game}/{choice.name}/{choice.name}_{number}.{image_ext}', filename=f"katana.{image_ext}")
            embed.set_image(url=f"attachment://katana.{image_ext}")
            await ctx.send(file=image, embed=embed)
        else:
            await ctx.send("Try Again!")



def setup(client):
    client.add_cog(KatanaInu(client))
