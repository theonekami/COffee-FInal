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
        self.Cp.set_collection("Cool Points")

    @commands.group(invoke_without_command=True)
    async def cp(self,ctx):
        await ctx.send("So, ....wheres the suffix")

    @cp.command(name="add")
    async def cp_add(self, ctx, args):
        x=ctx.message.mentions[0].id
##        await self.Cp.find(x)
        await self.Cp.insert(x = (ctx.message.mentions[0].name, 1))
        await ctx.send("Addded to"+ ctx.message.mentions[0].name)

    @cp.command(name="top")
    async def cp_top(self, ctx):
        await ctx.send(await self.Cp.print_db())

    @cp.command(name="find")
    async def cp_find(self, ctx):
        x= await self.Cp.find(y=ctx.message.mentions[0].id)
        y=x.to_list(1)
        await ctx.send(x)


def setup(bot):
    bot.add_cog(Cool_Point(bot))
