import discord
from discord.ext import commands
import json
import aiohttp
import dat


def basic_check(ctx):  ##for funsies
    if (ctx.author == ctx.guild.owner) or (ctx.author.id == 256390874848690176):
        return True
    else:
        return False



class Cool_Point:
    def __init__(self, bot):
        self.bot=bot
        self.Cp=dat.coolDb()
        self.Cp.set_collection("Coolpoints")

    @commands.group(invoke_without_command=True)
    async def cp(self,ctx):
        await ctx.send("So, ....wheres the suffix")

    @cp.command(name="add")
    async def cp_add(self, ctx):
        self.Cp.insert({str(ctx.message.mentions[0]):1})
        await ctx.send("Addded to" ctx.message.mentions[0])

def setup(bot):
    bot.add_cog(Cool_Point(bot))
