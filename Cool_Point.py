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
        store=bot.get_channel(id=500209038533984276)

    @commands.group(invoke_without_command=True)
    async def cp(self,ctx):
        await ctx.send("So, ....wheres the suffix")
##
##    @cp.command(name="add")
##    async def cp_add(self, ctx, args):
##        hm

def setup(bot):
    bot.add_cog(Cool_Point(bot))
