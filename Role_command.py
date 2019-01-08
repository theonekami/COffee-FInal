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


class Role_Commands:
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def gamenight(self,ctx):
        for i in ctx.guild.roles:
            if( i.name=="GameNight!"):
                x=i
        await ctx.author.add_roles(x)
        await ctx.send("You have the Gamenight Role! have fun")

    @commands.command()
    async def ungamenight(self,ctx):
        for i in ctx.guild.roles:
            if( i.name=="GameNight!"):
                x=i
        await ctx.author.remove_roles(x)
        await ctx.send("Un game nighted")

    @commands.command()
    async def dreamers(self,ctx):
        for i in ctx.guild.roles:
            if( i.name=="Dreamers"):
                x=i
        await ctx.author.add_roles(x)
        await ctx.send("You have the Dreamers Role! have fun")

    @commands.command()
    async def undreamers(self,ctx):
        for i in ctx.guild.roles:
            if( i.name=="Dreamers"):
                x=i
        await ctx.author.remove_roles(x)
        await ctx.send("Un dreamer'ed")

    @commands.command()
    async def hnf(self,ctx):
        for i in ctx.guild.roles:
            if( i.name=="h&f"):
                x=i
        await ctx.author.add_roles(x)
        await ctx.send("You have the Health and fitness Role! have fun")

    @commands.command()
    async def unhnf(self,ctx):
        for i in ctx.guild.roles:
            if( i.name=="h&f"):
                x=i
        await ctx.author.remove_roles(x)
        await ctx.send("Un h&f'd")


    @commands.command()
    async def cruise(self,ctx):
        for i in ctx.guild.roles:
            if( i.name=="Mephistopheles"):
                x=i
        await ctx.author.add_roles(x)
        await ctx.send("You have the Mephistopheles Role! have fun")

    @commands.command()
    async def uncruise(self,ctx):
        for i in ctx.guild.roles:
            if( i.name=="Mephistopheles"):
                x=i
        await ctx.author.remove_roles(x)
        await ctx.send("Un mephistopheles'd")


  
    @commands.command()
    async def ryan(self,ctx):
        for i in ctx.guild.roles:
            if( i.name=="?"):
                x=i
        await ctx.author.add_roles(x)
        await ctx.send("You have the ? Role! have fun")

    @commands.command()
    async def unryan(self,ctx):
        for i in ctx.guild.roles:
            if( i.name=="?"):
                x=i
        await ctx.author.remove_roles(x)
        await ctx.send("Un ?")

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
