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
    async def lin(self,ctx):
        x= ctx.message.role_mentions[0]
        y=""
        for i in x.members:
            y+=i.name+"\n"
        await ctx.author.send(y)
        await ctx.send("Sent dm")

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
    async def tournaments(self,ctx):
        x=None
        for i in ctx.guild.roles:
            if( i.name=="Tournaments"):
                x=i
        await ctx.author.add_roles(x)
        await ctx.send("You have the tour Role! have fun")

    @commands.command()
    async def untournaments(self,ctx):
        x=None
        for i in ctx.guild.roles:
            if( i.name=="Tournaments"):
                x=i
        await ctx.author.remove_roles(x)
        await ctx.send("Un toured. What a loser")

    @commands.command()
    async def lol(self,ctx):
        x=None
        for i in ctx.guild.roles:
            if( i.name=="Epic League Gamers"):
                x=i
        await ctx.author.add_roles(x)
        await ctx.send("You are an Epic League Gamer! have fun")

    @commands.command()
    async def unlol(self,ctx):
        x=None
        for i in ctx.guild.roles:
            if( i.name=="Epic League Gamers"):
                x=i
        await ctx.author.remove_roles(x)
        await ctx.send("Un Epic League Gamer'd. Ur worse than Faker")

    @commands.command()
    async def mtg(self,ctx):
        x=None
        for i in ctx.guild.roles:
            if( i.name=="MTG"):
                x=i
        await ctx.author.add_roles(x)
        await ctx.send("You have the mtg role. You are also a 3/3 Elk. have fun")

    @commands.command()
    async def pokemon(self,ctx):
        x=None
        for i in ctx.guild.roles:
            if( i.name=="Pokemon"):
                x=i
        await ctx.author.add_roles(x)
        await ctx.send("You have the pokemon Role! Sword and shield HYPE")

    @commands.command()
    async def unpokemon(self,ctx):
        x=None
        for i in ctx.guild.roles:
            if( i.name=="Pokemon"):
                x=i
        await ctx.author.remove_roles(x)
        await ctx.send("Un pokemon'd. You couldn't survive dexit")


    @commands.command()
    async def unmtg(self,ctx):
        x=None
        for i in ctx.guild.roles:
            if( i.name=="MTG"):
                x=i
        await ctx.author.remove_roles(x)
        await ctx.send("Un MTG'd. Sent to the exile")



    @commands.command()
    async def reader(self,ctx):
        x=None
        for i in ctx.guild.roles:
            if( i.name=="Heroes of Legend "):
                x=i
        await ctx.author.add_roles(x)
        await ctx.send("You have the Heroes of Legend  Role! have fun")

    @commands.command()
    async def unreader(self,ctx):
        x=None
        for i in ctx.guild.roles:
            if( i.name=="Heroes of Legend "):
                x=i
        await ctx.author.remove_roles(x)
        await ctx.send("Un Heroes of Legend  ;d")


    @commands.command()
    async def writing(self,ctx):
        x=None
        for i in ctx.guild.roles:
            if( i.name=="Writing Advice"):
                x=i
        await ctx.author.add_roles(x)
        await ctx.send("May your words flow true.")

    @commands.command()
    async def unwriting(self,ctx):
        x=None
        for i in ctx.guild.roles:
            if( i.name=="Writing Advice"):
                x=i
        await ctx.author.remove_roles(x)
        await ctx.send("Un writing'd. Your words will not be forgotten")


        

                

def setup(bot):
    bot.add_cog(Role_Commands(bot))
