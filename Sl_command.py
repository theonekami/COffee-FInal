import discord
from discord.ext import commands
import json
import aiohttp
import random

races= ["Human","Elf","Pixie","Arakora","Pureblood","Lycan","Triton","Tortle","Lizardfolk","Kobold","Kenku","Halfling","Goblin","Gensai","Elemental","aasimar","Tiefling,","Thrikeen","Void"]

patron= ["Apollo","Bard","BattleBorn","Satan","Leviathan","Beelzebub","Gaia","Prom","Atlas"]

def show_check(ctx,args):
    return ((args=="Show" or args=="show" or args=="s"))


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
        world= "https://docs.google.com/document/d/1CtqNIBIx4RhXTlxJv1d15ZwPv3ntTWt00pX04NfqmPU/edit"
        em.add_field(name="Heroes of Legend" ,value = world)
        if(show_check(ctx,args)):
            await ctx.send(embed=em)
        else:
            await ctx.author.send(embed=em)
            await ctx.send("Look into your dms....")

    @commands.command() 
    async def sl(self,ctx,args=None):
        em = discord.Embed(title="Docs")
        s="""
    Main doc:\nhttps://docs.google.com/document/d/1CtqNIBIx4RhXTlxJv1d15ZwPv3ntTWt00pX04NfqmPU/edit
    
    Inventory: \nhttps://docs.google.com/document/d/1N0ZzCGZk85GTmt8P2uZRuCOLmkIWS9xuFxuLmjM4URU/edit
 
    HQ: \nhttps://docs.google.com/document/d/1ontKMMgFREqkas6YlOHe_DtU1DHWF8JyCbBQP1GXwn0/edit

    """
        em.add_field(name="Starless", value = s)
        if(show_check(ctx,args)):
            await ctx.send(embed=em)
        else:
            await ctx.author.send(embed=em)
            await ctx.send("Look into your dms....")



def setup(bot):
    bot.add_cog(SL_Stuffs(bot))
