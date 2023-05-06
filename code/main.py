import discord
import random
import sqlite3
import os
from discord import Embed, File, Game
from discord.ext import commands, tasks
from discord.ext.commands import cooldown, BucketType
from dotenv import load_dotenv
from itertools import cycle
from KatanaInu import KatanaInu


client = commands.Bot(command_prefix="!", help_command=None, case_insensitive=True, intents=discord.Intents.all())
load_dotenv()
TOKEN = os.getenv("TOKEN")

extensions = [KatanaInu(client)]
status = cycle([
    "!help", 
    "!katanainu", 
    "!help nsfw", 
    "!download", 
    "!invite", 
    "!gm", 
    "!gn",
    "!join"
])

async def update_status():
    await client.wait_until_ready()
    while not client.is_closed():
        current_status = next(status)
        game = Game(name=current_status)
        await client.change_presence(activity=game, status="online", 
                                      afk=False,)
        await asyncio.sleep(5)                             

@client.event
async def on_ready():
    for extension in extensions:
        try:
            await client.add_cog(extension)
            print(f"loaded {extension}!")
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))
    changeGameActivity.start()
    print("Hello there!")


@tasks.loop(seconds=7)
async def changeGameActivity():
    await client.change_presence(activity=discord.Game(next(status)))


@client.command()
async def socials(ctx):
    title = "KatanaInu Social Media"
    website= "https://www.katanainu.com/"
    marketplace= "https://kainu.io/"
    telegram= "https://t.me/katanainu"
    youtube= "https://www.youtube.com/channel/UCD3HhRKj28mj3PxYCwxjddg"
    instagram= "https://instagram.com/katanainu"
    tiktok= "https://www.tiktok.com/@katanainu"
    reddit= "https://www.reddit.com/r/katanainu/"
    twitter= " https://twitter.com/katanainu"
    opensea= " https://opensea.io/collection/katanainu-takeru"
    looksrare= "https://bit.ly/3qmcyoB"
    uniswap= "https://bit.ly/3iovcYl"
    dextool="https://bit.ly/3D0wx0R"
    pankcake="https://bit.ly/3ilAPGK"

    image_url = "https://cdn.discordapp.com/attachments/1090598600008024105/1104404021101469718/1500x500.png"
    embed = discord.Embed(title=title, description="You can easily access all our social media addresses here.", url="https://www.katanainu.com/")
    embed.set_image(url=image_url)
    embed.add_field(name="Website:", value=website, inline=False)
    embed.add_field(name="Kainu - Marketplace:", value=marketplace, inline=False)
    embed.add_field(name="Telegram :", value=telegram, inline=False)
    embed.add_field(name="Youtube :", value=youtube, inline=False)
    embed.add_field(name="Instagram :", value=instagram, inline=False)
    embed.add_field(name="TikTok :", value=tiktok, inline=False)
    embed.add_field(name="Reddit :", value=reddit, inline=False)
    embed.add_field(name="Twitter :", value=twitter, inline=False)
    embed.add_field(name="OpenSea :", value=opensea, inline=False)
    embed.add_field(name="LooksRare :", value=looksrare, inline=False)
    embed.add_field(name="Uniswap $KATA ETH :", value=uniswap, inline=False)
    embed.add_field(name="Dextools ETH Chart :", value=dextool, inline=False)
    embed.add_field(name="PancakeSwap $KATA BSC :", value=pankcake, inline=False)
    await ctx.send(embed=embed)

@client.command()
async def download(ctx):
    title = "Download the KatanaInu Game"
    download = "https://play.katanainu.com/"

    image_url = "https://cdn.discordapp.com/attachments/1090598600008024105/1104404021101469718/1500x500.png"
    embed = discord.Embed(title=title, description="You can easily invite EdenXverse Bot to your server by clicking the link.", url="https://edenxverse.itch.io/ar")
    embed.set_image(url=image_url)
    embed.add_field(name="Download", value=download, inline=False)
    await ctx.send(embed=embed)
    
@client.command()
async def about(ctx):
    title = "About KatanaInu"
    about = "https://katanainu.com/about"

    image_url = "https://cdn.discordapp.com/attachments/1090598600008024105/1104404021101469718/1500x500.png"
    embed = discord.Embed(title=title, description="Katana Inu promotes gaming innovation by efficiently merging two revolutionary technologies — gaming and blockchain.As an all-encompassing ecosystem for gamers and traders, powered by DeFi and NFT, Katana Inu's objective is simple: to create a system where gamers can earn from their playtime. Over 1 billion PC gamers play traditional games for several hours daily without profiting from their grind. We hope to change this by developing a unique Play-to-Earn battle royale PC game with NFT mechanics. This approach is the central concept behind Katana Inu! The game comes with rare NFT skins and high graphics to lure players from the blockchain and NFT space and a portion of the 1 billion players of traditional PC games. Katana Inu has a native cross-chain NFT marketplace, which is open to Katana Inu players, regular art dealers, and gamers from other NFT projects.", url="https://katanainu.com/about")
    embed.set_image(url=image_url)
    embed.add_field(name="For More Info", value=about, inline=False)
    await ctx.send(embed=embed)
    
@client.command()
async def team(ctx):
    title = "KatanaInu Team"
    marwan = " CEO & FOUNDER"
    hamza="COO"
    yezdan="Marketing Manager"
    image_url = "https://cdn.discordapp.com/attachments/1090598600008024105/1104404021101469718/1500x500.png"
    embed = discord.Embed(title=title, description="OUR TEAM MEMBERS", url="https://katanainu.com/team")
    embed.set_image(url=image_url)
    embed.add_field(name="Marwan H", value=marwan, inline=False)
    embed.add_field(name="Hamza S.", value=hamza, inline=False)
    embed.add_field(name="Yezdan N.", value=yezdan, inline=False)
    await ctx.send(embed=embed)
    

@client.command()
async def help(ctx, plugin=None):
    title = "KatanaInu commands!"
    description = "Which category would you like to get the help commands from?\KatanaInu supports the following modules:"

    field_names = []
    field_values = []
    if plugin is None:

        field_names.append("__KatanaInu__")
        field_values.append("Commands for our KatanaInu Bot plugin! (!katanainu)")
        field_names.append("__Team__")
        field_values.append("Commands for our KatanaInu Bot plugin! (!team)")
        field_names.append("__About__")
        field_values.append("Commands for our KatanaInu Bot plugin! (!about)")
        field_names.append("__Download__")
        field_values.append("Commands for our KatanaInu Bot plugin! (!download)")
        field_names.append("__Socil Media Links__")
        field_values.append("Commands for our KatanaInu Bot plugin! (!socials)")

    footer = "Let's Fun!"

    embed = discord.Embed(title=title, description=description, color=0xFFA800)
    embed.set_footer(text=footer)

    for i in range(0, len(field_names)):
        embed.add_field(name=field_names[i], value=field_values[i], inline=False)

    await ctx.send(embed=embed)


if __name__ == '__main__':
    client.run(TOKEN)
