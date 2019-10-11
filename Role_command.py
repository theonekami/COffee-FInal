import discord
from discord.ext import commands
import json
import aiohttp


def basic_check(ctx):  ##for funsies
    p=ctx.author
    for i in p.roles:
        if i.name=="Moderator":
            return True
    if (p == ctx.guild.owner) or (p == 256390874848690176):
        return True
    else:
        return False


class Role_Commands(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def gamenight(self,ctx):
        x=None
        for i in ctx.guild.roles:
            if( i.name=="GameNight!"):
                x=i
        await ctx.author.add_roles(x)
        await ctx.send("You have the Gamenight Role! have fun")

    @commands.command()
    async def ungamenight(self,ctx):
        x=None
        for i in ctx.guild.roles:
            if( i.name=="GameNight!"):
                x=i
        await ctx.author.remove_roles(x)
        await ctx.send("Un game nighted")

    @commands.command()
    async def dreamers(self,ctx):
        x=None
        for i in ctx.guild.roles:
            if( i.name=="Dreamers"):
                x=i
        await ctx.author.add_roles(x)
        await ctx.send("You have the Dreamers Role! have fun")

    @commands.command()
    async def undreamers(self,ctx):
        x=None
        for i in ctx.guild.roles:
            if( i.name=="Dreamers"):
                x=i
        await ctx.author.remove_roles(x)
        await ctx.send("Un dreamer'ed")

    @commands.command()
    async def orbis(self,ctx):
        x=None
        for i in ctx.guild.roles:
            if( i.name=="Orbis"):
                x=i
        await ctx.author.add_roles(x)
        await ctx.send("You have the Orbis Role! have fun")

    @commands.command()
    async def unorbis(self,ctx):
        x=None
        for i in ctx.guild.roles:
            if( i.name=="Orbis"):
                x=i
        await ctx.author.remove_roles(x)
        await ctx.send("Un orbis'ed")

    @commands.command()
    async def hnf(self,ctx):
        x=None
        for i in ctx.guild.roles:
            if( i.name=="h&f"):
                x=i
        await ctx.author.add_roles(x)
        await ctx.send("You have the Health and fitness Role! have fun")

    @commands.command()
    async def unhnf(self,ctx):
        x=None
        for i in ctx.guild.roles:
            if( i.name=="h&f"):
                x=i
        await ctx.author.remove_roles(x)
        await ctx.send("Un h&f'd")

    @commands.command()
    async def pmd(self,ctx):
        x=None
        for i in ctx.guild.roles:
            if( i.name=="Cryosis"):
                x=i
        await ctx.author.add_roles(x)
        await ctx.send("You have the pmd Role! have fun")

    @commands.command()
    async def unpmd(self,ctx):
        x=None
        for i in ctx.guild.roles:
            if( i.name=="Cryosis"):
                x=i
        await ctx.author.remove_roles(x)
        await ctx.send("Un pmd'd")

   @commands.command()
    async def monotour(self,ctx):
        x=None
        for i in ctx.guild.roles:
            if( i.name=="MonotypeTour"):
                x=i
        await ctx.author.add_roles(x)
        await ctx.send("You have the mono type tour Role! have fun")

    @commands.command()
    async def unmonotour(self,ctx):
        x=None
        for i in ctx.guild.roles:
            if( i.name=="MonotypeTour"):
                x=i
        await ctx.author.remove_roles(x)
        await ctx.send("Un toured. What a loser")


##    @commands.command()
##    async def reader(self,ctx):
##        x=None
##        for i in ctx.guild.roles:
##            if( i.name=="HEROES LEGENDARY BOOKS AND ARCANA MAGIC"):
##                x=i
##        await ctx.author.add_roles(x)
##        await ctx.send("You have the HEROES LEGENDARY BOOKS AND ARCANA MAGIC Role! have fun")
##
##    @commands.command()
##    async def unreader(self,ctx):
##        x=None
##        for i in ctx.guild.roles:
##            if( i.name=="HEROES LEGENDARY BOOKS AND ARCANA MAGIC"):
##                x=i
##        await ctx.author.remove_roles(x)
##        await ctx.send("Un HEROES LEGENDARY BOOKS AND ARCANA MAGIC ;d")
##
##
   

    @commands.command()
    @commands.check(basic_check)
    async def mute(self,ctx,args):
        for i in ctx.guild.roles:
            if( i.name=="Locked"):
                x=i
        for i in ctx.guild.members:
            if(i.mentioned_in(ctx.message)):
                await i.add_roles(x)
        await ctx.send("Muted Get REKT")

    @commands.command()
    @commands.check(basic_check)
    async def unmute(self,ctx,args):
        for i in ctx.guild.roles:
            if( i.name=="Locked"):
                x=i
        for i in ctx.guild.members:
            if(i.mentioned_in(ctx.message)):
                await i.remove_roles(x)
        await ctx.send("Unmuted")
        

                

def setup(bot):
    bot.add_cog(Role_Commands(bot))
