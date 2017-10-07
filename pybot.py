import datetime
import discord
import time
from discord.ext import commands

prefix = 'p!'

description = 'PyBot - A Python remake of PiBot. Developed by LeoPiGuy'

extensions = ('cogs.info', "cogs.pi")

bot = commands.Bot(command_prefix=prefix, description=description)

@bot.event
async def on_ready():
    print("Logged in as: {0.user.name} | {0.user.id}".format(bot))
    print("----------------------------------------")
    print("")

    await bot.change_presence(game=discord.Game(name='Redeveloping as PyBot!'))

    if __name__ == '__main__':
        for extension in extensions:
            await load(extension)

async def load(extension):
    try:
        bot.load_extension(extension)
        print("Loaded Extension: {}".format(extension))
    except Exception as e:  
        exc = '{}: {}'.format(type(e).__name__, e)
        print('Failed to load cog: {}\n{}'.format(extension, exc))

async def unload(extension):
    bot.unload_extension(extension)
    print("{} unloaded.".format(extension))

@bot.command()
async def reload(ctx, arg):
    print("-----------------------")
    print("Reloading Extension: {}".format(arg))
    await unload("cogs.{}".format(arg))
    await load("cogs.{}".format(arg))
    print("-----------------------")


