import discord
import pidigits
from pidigits import getPi
from discord.ext import commands

class Pi:
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def pi(self, ctx, arg):
        #if arg.isdigit():
            num = int(arg)
            if num < 1994 and num > 0:
                digits = getPi(num)
                del digits[0]
                numbers = "".join(str(item) for item in digits)
                await ctx.send("```3.{}```".format(numbers))
            else:
                await ctx.send("Number out of range. Must be between 1 and 1993.")
        #else:
            await ctx.send("Invalid Number. Must be a positive integer.")

    @pi.error
    async def pi_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Not Enough Arguments: Please include how many digits of pi you want computed.")

    @commands.command()
    async def pie(self, ctx):
        await ctx.send("https://cdn.nashvillescene.com/files/base/scomm/nvs/image/2017/03/960w/pi_day.58c2cf87a0dd8.jpg")

def setup(bot):
    bot.add_cog(Pi(bot))