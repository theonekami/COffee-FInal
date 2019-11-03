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


class SL_Stuffs(commands.Cog):
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
    async def map(self,ctx,args=1):
        x="https://cdn.discordapp.com/attachments/534369484572590100/534371722330112001/1.PNG"
        await ctx.send(x)
        
    @commands.command() 
    async def docs(self,ctx,args=None):
        world =" https://docs.google.com/document/d/1Gtmtni5J_738VEJSc7aH1L3_fxoB1BRpPvaUTmMRxss/edit?usp=sharing"
        em.add_field(name="Under the Surface" ,value ="SCP inspired rp where you’re part of a secret agency trying to stop creatures from inhabiting our world\n" + world)
        
        if(show_check(ctx,args)):
            await ctx.send(embed=em)
        else:
            await ctx.author.send(embed=em)
            await ctx.send("Look into your dms....")

##    @commands.command() 
##    async def hol(self,ctx,args=None):
##        em = discord.Embed(title="Docs")
##        s="""
##    Main doc:\nhttps://docs.google.com/document/d/1CtqNIBIx4RhXTlxJv1d15ZwPv3ntTWt00pX04NfqmPU/edit
##    
##    Inventory: \nhttps://docs.google.com/document/d/1N0ZzCGZk85GTmt8P2uZRuCOLmkIWS9xuFxuLmjM4URU/edit
## 
##    HQ: \nhttps://docs.google.com/document/d/1ontKMMgFREqkas6YlOHe_DtU1DHWF8JyCbBQP1GXwn0/edit
##
##    """
##        em.add_field(name="Heroes Of legend", value = s)
##        if(show_check(ctx,args)):
##            await ctx.send(embed=em)
##        else:
##            await ctx.author.send(embed=em)
##            await ctx.send("Look into your dms....")

    @commands.command() 
    async def cry(self,ctx,args=None):
        em = discord.Embed(title="Docs")
        s="""
Main doc:\nhttps://docs.google.com/document/d/1LcozKEI-p345W1o_L6dyy83wRDPIk_y-N80zLY5SGqg/edit
\n Players:\nhttps://docs.google.com/spreadsheets/d/1JfU3WyXdj2qHG1nnrE3atWxtYypHBQBL6zSQ-BZUHHE/edit#gid=0
\n Town:\n https://docs.google.com/document/d/1-R3fVpMidh2b8ekPuf8dDY4A1bOyXrOu6B6Ym5w1D_o/edit
\n Map:\n https://docs.google.com/document/d/1I1DpCQWvQVY_TgzDyRLKpbwB536b7n2QP7sEJD2RG0A/edit
    """
        em.add_field(name="Cryosis", value = s)
        if(show_check(ctx,args)):
            await ctx.send(embed=em)
        else:
            await ctx.author.send(embed=em)
            await ctx.send("Look into your dms....")



def setup(bot):
    bot.add_cog(SL_Stuffs(bot))
