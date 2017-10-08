import datetime
import discord
import time
from discord.ext import commands

prefix = 'p!'

description = 'PyBot - A Python remake of PiBot. Developed by LeoPiGuy'

extensions = ('cogs.info', "cogs.pi")

loaded_extensions = []

bot = commands.Bot(command_prefix=prefix, description=description)

@bot.event
async def on_ready():
    print("Logged in as: {0.user.name} | {0.user.id}".format(bot))
    print("----------------------------------------")
    print("")

    await bot.change_presence(game=discord.Game(name='Redeveloping as PyBot!'))

def load(extension):
    try:
        bot.load_extension(extension)
        print("Loaded Extension: {}".format(extension))

        return False
    except Exception as e:  
        exc = '{}: {}'.format(type(e).__name__, e)
        print('Failed to load cog: {}\n{}'.format(extension, exc))
        return exc

def unload(extension):
    bot.unload_extension(extension)
    print("{} unloaded.".format(extension))

@bot.command(hidden=True)
async def reload(ctx, arg):
    print("-----------------------")
    print("Reloading Extension: {}".format(arg))
    unload("cogs.{}".format(arg))
    err = load("cogs.{}".format(arg))
    if err:
        await ctx.send("```Failed to load extension {}.\n{}```".format(arg, err))
    else:
        await ctx.send("`Reloaded Extension {}!`".format(arg))
    print("-----------------------")

@bot.command(hidden=True)
async def listcogs(ctx):
    string = " , ".join(str(cog) for cog in loaded_extensions)
    await ctx.send("`Loaded Extensions: {}`".format(string))

if __name__ == '__main__':
    for extension in extensions:
        err = load(extension)
        if not err:
            loaded_extensions.append(extension[5:])
