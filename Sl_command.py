import discord
from discord.ext import commands
import json
import aiohttp
import random

races= ["Human","Elf","Pixie","Arakora","Pureblood","Lycan","Triton","Tortle","Lizardfolk","Kobold","Kenku","Halfling","Goblin","Gensai","Elemental","aasimar","Tiefling,","Thrikeen","Void"]

patron= ["Apollo","Bard","BattleBorn","Satan","Leviathan","Beelzebub","Gaia","Prom","Atlas"]



def basic_check(ctx):  ##for funsies
    if (ctx.author == ctx.guild.owner) or (ctx.author.id == 256390874848690176):
        return True
    else:
        return False


class SL_Stuffs:
    def __init__(self, bot):
        self.bot=bot
        
    @commands.command()
    async def randrace(self,ctx,args=1):
        'A pick device. Uses a list so i think any number of arguments can work'
        x=""
        for i in range(0,args):
            x += random.choice(races)+ ","
        await ctx.send('Umm..I Picked: ' + x)

    @commands.command()
    async def randpatron(self,ctx,args=1):
        'A pick device. Uses a list so i think any number of arguments can work'
        x=""
        for i in range(0,args):
            x += random.choice(patron)+","
        await ctx.send('Umm..I Picked: ' + x)
        
    @commands.command() 
    async def docs(self,ctx,args=None):
        em = discord.Embed(title="Docs")
        em.add_field(name="Starless" ,value="https://docs.google.com/document/d/1dYwKxoP0o1WVeSyb8ptrrmm7of73YHb7Ru97pGBJX9I/edit'")
        world= "https://docs.google.com/document/d/1NHoizFrN5MFiqWZKv1g7aHSiVfZbbT-NJAppnBj9e14/edit"
        em.add_field(name="World Eaters" ,value = world)
        if(show_check(ctx,args)):
            await ctx.send(embed=em)
        else:
            await ctx.author.send(embed=em)
            await ctx.send("Look into your dms....")

    @commands.command() 
    async def sl(self,ctx):
        em = discord.Embed(title="Docs")
        s="""
    Main doc:\nhttps://docs.google.com/document/d/1dYwKxoP0o1WVeSyb8ptrrmm7of73YHb7Ru97pGBJX9I/edit

    Inventory: \nhttps://docs.google.com/document/d/1ULrJfzj9rd7Pd7SHX_0pgcrXLLR77q5qvGk04OSZteQ/edit 


    Shops:\nhttps://docs.google.com/document/d/1k6ivv_ljadAuKqQ2st1kDrIt9x2-vHogqU5Q8S6n0yA/edit
    \n https://docs.google.com/document/d/1IieJwLf7mGsBjMlmEYO2A4J3lYNcHEEm7aZ-NQEscJY/edit 
    """
        em.add_field(name="Starless", value = s)
        if(show_check(ctx,args)):
            await ctx.send(embed=em)
        else:
            await ctx.author.send(embed=em)
            await ctx.send("Look into your dms....")



def setup(bot):
    bot.add_cog(SL_Stuffs(bot))
