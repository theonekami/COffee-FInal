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
        em = discord.Embed(title="Docs")
        world= "https://docs.google.com/document/d/1CtqNIBIx4RhXTlxJv1d15ZwPv3ntTWt00pX04NfqmPU/edit"
        em.add_field(name="Heroes of Legend" ,value ="The world of Creata is as peaceful as it'll ever be. Your oc is a reader. A special person in this world of normal mages. What does that mean for you? will you be Silent  , or will you rise to the top. \n" + world)
        world =" https://docs.google.com/document/d/1-rYrfoVzTCu13eQMPs96ZEJ1-I9Oq-Iek-A1EKD3XLY/edit"
        em.add_field(name="Darkest Dungeons Second chance" ,value ="Darkest Dungeons inspired DND. Uses unique combat mechanics and challenges teamwork.\n" + world)
        world =" https://docs.google.com/document/d/1Gtmtni5J_738VEJSc7aH1L3_fxoB1BRpPvaUTmMRxss"
        em.add_field(name="Under the Surface" ,value ="SCP inspired rp where you’re part of a secret agency trying to stop creatures from inhabiting our world\n" + world)
        world =" https://docs.google.com/document/d/1-rYrfoVzTCu13eQMPs96ZEJ1-I9Oq-Iek-A1EKD3XLY/edit"
        em.add_field(name="Steam Blood fantasy" ,value ="Warhammer inspired RP with some anime where you're place in a war between humanity and the vampires before their known world becomes bigger.\n" + world)
        
        if(show_check(ctx,args)):
            await ctx.send(embed=em)
        else:
            await ctx.author.send(embed=em)
            await ctx.send("Look into your dms....")

    @commands.command() 
    async def hol(self,ctx,args=None):
        em = discord.Embed(title="Docs")
        s="""
    Main doc:\nhttps://docs.google.com/document/d/1CtqNIBIx4RhXTlxJv1d15ZwPv3ntTWt00pX04NfqmPU/edit
    
    Inventory: \nhttps://docs.google.com/document/d/1N0ZzCGZk85GTmt8P2uZRuCOLmkIWS9xuFxuLmjM4URU/edit
 
    HQ: \nhttps://docs.google.com/document/d/1ontKMMgFREqkas6YlOHe_DtU1DHWF8JyCbBQP1GXwn0/edit

    """
        em.add_field(name="Heroes Of legend", value = s)
        if(show_check(ctx,args)):
            await ctx.send(embed=em)
        else:
            await ctx.author.send(embed=em)
            await ctx.send("Look into your dms....")



def setup(bot):
    bot.add_cog(SL_Stuffs(bot))
