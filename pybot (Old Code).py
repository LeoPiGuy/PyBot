import datetime
import discord
import time
from discord.ext import commands

prefix = 'p!'
description = 'PyBot - A Python remake of PiBot. Developed by Leo Gold'
extensions = ('cogs.info', "cogs.pi", "cogs.memes")
# client = discord.Client()
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
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#     if message.content.startswith('{}hello'.format(prefix)):
#         await message.channel.send('Hello!')
#     elif message.content.startswith('{}heartbeat'.format(prefix)):
#         heartbeat = client.latency
#         await message.channel.send('Heartbeat: `{}ms`'.format(heartbeat))
#     elif message.content.startswith('{}ping'.format(prefix)):
#         currentTime = datetime.datetime.utcnow()
#         sentMessage = await message.channel.send('Pong!')
#         duration = currentTime-sentMessage.created_at
#         print(duration.microseconds/1000)
#         await sentMessage.edit(content="Pong! Took `{}ms`".format(duration.microseconds/1000))
#     elif message.content.startswith('{}stop'.format(prefix)):
#         if message.author.id == 268044207854190604:
#             await message.channel.send('{} Shutting Down...'.format(client.user.display_name))
#             raise SystemExit
#     elif message.content.startswith(prefix):
#         await message.channel.send("Invalid command!")

# @bot.command()
# async def hello(ctx):
#     await ctx.send("Hello!")

# @bot.command()
# async def heartbeat(ctx):
#     pingTime = bot.latency
#     await ctx.send('Heartbeat: `{}ms`'.format(float(pingTime)*1000))

# @bot.command()
# async def ping(ctx):
#     currentTime = datetime.datetime.utcnow()
#     sentMessage = await ctx.send('Pong!')
#     duration = currentTime-sentMessage.created_at
#     print(duration.microseconds/1000)
#     await sentMessage.edit(content="Pong! Took `{}ms`".format(duration.microseconds/1000)) 

# @bot.command()
# async def stop(ctx):
#     if ctx.author.id == 268044207854190604:
#         sentMessage = await ctx.send('{} Shutting Down.'.format(bot.user.display_name))
#         time.sleep(5)
#         await sentMessage.delete()
#         raise SystemExit

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


