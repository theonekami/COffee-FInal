import discord
from discord.ext import commands
import json
import aiohttp



def basic_check(ctx):  ##for funsies
    if (ctx.author == ctx.guild.owner) or (ctx.author.id == 256390874848690176):
        return True
    else:
        return False


class Cool_Point(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
        self.channel_id=642950089719021629
        self.rf=self.bot.get_channel(id=self.channel_id)


##    @commands.command()
##    async def kek(self, ctx, args):
##        await self.store.send(args)
##    
    @commands.group(invoke_without_command=True)
    async def cf(self,ctx):
        pass

    @cf.command(name="reg")
    async def cf_register(self, ctx):
        new=ctx.message.mentions[0]
        async for i in self.rf.history(limit=100):
            if new.id in i:
                ctx.send("User already in!")
                return
        await self.rf.send(str(new) +"|" + str(new.id)+ "|" + "1" + "|"+ "Dummy1")
        await ctx.send("Added "+ str(ctx.message.mentions[0]))

def setup(bot):
    bot.add_cog(Cool_Point(bot))
