import discord
from discord.ext import commands

class PiCog:
    def __init__(self, bot):
        self.bot=bot
        type(self).__name__ = 'Pi'

    @commands.command()
    async def pi(self, ctx, arg):
        ctx.send("3.1415926...")

def setup(bot):
    bot.add_cog(PiCog(bot))