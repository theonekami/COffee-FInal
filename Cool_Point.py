import discord
from discord.ext import commands
import json
import aiohttp



def basic_check(ctx):  ##for funsies
    if (ctx.author == ctx.guild.owner) or (ctx.author.id == 256390874848690176):
        return True
    else:
        return False


class Cool_Point:
    def __init__(self, bot):
        self.bot=bot
        self.store=bot.get_channel(id=500209038533984276)
        self.num

##    @commands.command()
##    async def kek(self, ctx, args):
##        await self.store.send(args)
##    
    @commands.group(invoke_without_command=True)
    async def cp(self,ctx):
        await ctx.send("So, ....wheres the suffix")

    @cp.command(name="add")
    async def cp_add(self, ctx,*, args):
        num=args.split()
        v=0
        for i in num:
            try:
                v=int(i)
            except:
                continue
        print(v)
        person=ctx.message.mentions[0]
        msg=str(person.id)+"|" + str(person.name)+"|"+str(args)
        await self.store.send(msg)
        

def setup(bot):
    bot.add_cog(Cool_Point(bot))
