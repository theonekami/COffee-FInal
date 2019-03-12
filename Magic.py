import discord
from discord.ext import commands
import json
import aiohttp

class Magic(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def card(self,ctx,*,args):
        x=str(args)
        x=x.replace(" ","%20")      
        y=None
        z='https://api.magicthegathering.io/v1/cards?name="'+x+'"'
        print(z)
        async with aiohttp.request("get","https://api.scryfall.com/cards/named?fuzzy="+x) as res:
            print(res.status)
            y=json.loads(await res.text())
        res.close()
        if(y['object']=="card"):
            em = discord.Embed(title=y['name'])
            em.set_image(url=y["image_uris"]['border_crop'])
            await ctx.send(embed= em)
        elif(y['object']=="error"):
            await ctx.send(y["details"])


    @commands.group()
    async def mg(self,ctx,*,args):
        pass

    @mg.command(name="commander")
    async def magic_commn(self,ctx,*,args):
        x=str(args)
        x=x.replace(" ","%20")      
        y=None
        z='https://api.magicthegathering.io/v1/cards?name="'+x+'"'
        print(z)
        async with aiohttp.request("get","https://api.scryfall.com/cards/random?q=is%3Acommander") as res:
            print(res.status)
            y=json.loads(await res.text())
        res.close()
        if(y['object']=="card"):
            em = discord.Embed(title=y['name'])
            em.set_image(url=y["image_uris"]['border_crop'])
            await ctx.send(embed= em)
        elif(y['object']=="error"):
            await ctx.send(y["details"])

##    @magic.command(name="Art")
##    async def magic_art(self ,ctx, *,args):
##        x=str(args)
##        x=x.replace(" ","%20")      
##        y=None
##        z='https://api.magicthegathering.io/v1/cards?name="'+x+'"'
##        print(z)
##        async with aiohttp.request("get","https://api.scryfall.com/cards/named?fuzzy="+x) as res:
##            print(res.status)
##            y=json.loads(await res.text())
##        res.close()
##        if(y['object']=="card"):
##            em = discord.Embed(title=y['name'])
##            em.set_image(url=y["image_uris"]['art_crop'])
##            await ctx.send(embed= em)
##        elif(y['object']=="error"):
##            await ctx.send(y["details"])
    

        
class Yugi(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def ycard(self,ctx,*,args):
        x=str(args)
        x=x.replace(" ","%20")
        y=None
        z="https://db.ygoprodeck.com/api/v3/cardinfo.php?name="+x
        print(z)
        async with aiohttp.request("get",z) as res:
            print(res.status)
            y=json.loads(await res.text())
        res.close()
        try:
                
            em = discord.Embed(title=y[0][0]['name'])
            em.set_image(url=y[0][len(y[0])-1]["image_url"])
            await ctx.send(embed= em)
        except:
            await ctx.send("Card name " + str(args) + " not found")
##

##class HS:
##    def __init__(self, bot):
##        self.bot=bot
##
##    @commands.command()
##    async def hscard(self,ctx,args):
##        x=str(args)
##        x=x.replace(" ","%20")
##        y=None
##        h={"X-Mashape-Key": "nZsSdxxcN1mshskGiEd18AIpXDksp19XabQjsn8LotoIfnfv54","Accept": "application/json"}
##        async with aiohttp.get("https://omgvamp-hearthstone-v1.p.mashape.com/cards/"+x,headers=h)) as res:
##            print(res.status)
##            y=json.loads(await res.text())
##        res.close()
##        try:
##            em = discord.Embed(title=y[[0]['name'])
##            em.set_image(url=y[0]['img'])
##            await ctx.send(embed= em)
##        except:
##            await ctx.send("Card name " + str(args) + " not found")

def setup(bot):
    bot.add_cog(Magic(bot))
    bot.add_cog(Yugi(bot))
