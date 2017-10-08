import discord
import time, datetime
from discord.ext import commands

class Utility:
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello!")
    
    @commands.command()
    async def heartbeat(self, ctx):
        pingTime = self.bot.latency
        await ctx.send('Heartbeat: `{}ms`'.format(float(pingTime)*1000))

    @commands.command()
    async def ping(self, ctx):
        currentTime = datetime.datetime.utcnow()
        sentMessage = await ctx.send('Pong!')
        duration = currentTime-sentMessage.created_at
        print(duration.microseconds/1000)
        await sentMessage.edit(content="Pong! Took `{}ms`".format(duration.microseconds/1000))
    
    @commands.command(hidden=True)
    async def stop(self, ctx):
        if ctx.author.id == 268044207854190604:
            sentMessage = await ctx.send('{} Shutting Down.'.format(self.bot.user.display_name))
            time.sleep(1)
            await sentMessage.delete()
            raise SystemExit

def setup(bot):
    bot.add_cog(Utility(bot))