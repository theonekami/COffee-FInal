import discord
from discord.ext import commands
import json
import aiohttp


class Net_Commands(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.command()
    async def cat(self, ctx):
        em = discord.Embed(title="Cat Pix")
        async with aiohttp.request("get","http://thecatapi.com/api/images/get") as res:
            em.set_image(url=res.url)
        res.close()
        await ctx.send(embed= em)

    @commands.command()
    async def dog(self,ctx):
        em = discord.Embed(title="Doggo Pix")
        async with aiohttp.request("get","https://dog.ceo/api/breeds/image/random") as res:
            x= json.loads(await res.text())
        res.close()
        em.set_image(url=x['message'])
        await ctx.send(embed= em)

    @commands.command()
    async def fox(self,ctx):
        em = discord.Embed(title="Fox Pix")
        async with aiohttp.request("get","https://randomfox.ca/floof/") as res:
            x= json.loads(await res.text())
        res.close()
        em.set_image(url=x['image'])
        await ctx.send(embed= em)

    @commands.command()
    async def birb(self,ctx):
        em = discord.Embed(title="birb pics")
        async with aiohttp.request("get","http://shibe.online/api/birds") as res:
            x= json.loads(await res.text())
        res.close()
        em.set_image(url=x[0])
        await ctx.send(embed= em)

    @commands.command()
    async def hug(self,ctx):
        em=em = discord.Embed(title="HUGGGSSSSS!!!!")
        async with aiohttp.request("get","https://some-random-api.ml/animu/hug") as res:
            x=json.loads(await res.text())
        res.close()
        em.set_image(url=x["link"])
        await ctx.send(embed=em)

    @commands.command()
    async def pet(self,ctx):
        em=em = discord.Embed(title="There There")
        async with aiohttp.request("get","https://some-random-api.ml/animu/pat") as res:
            x=json.loads(await res.text())
        res.close()
        em.set_image(url=x["link"])
        await ctx.send(embed=em)

    @commands.command()
    async def panda(self,ctx):
        em=em = discord.Embed(title="PANDAAA!!!!")
        async with aiohttp.request("get","https://some-random-api.ml/img/panda") as res:
            x=json.loads(await res.text())
        res.close()
        em.set_image(url=x["link"])
        await ctx.send(embed=em)

    @commands.command()
    async def red_panda(self,ctx):
        em=em = discord.Embed(title="Red panda!!!!")
        async with aiohttp.request("get","https://some-random-api.ml/img/red_panda") as res:
            x=json.loads(await res.text())
        res.close()
        em.set_image(url=x["link"])
        await ctx.send(embed=em)

    @commands.command()
    async def koala(self,ctx):
        em=em = discord.Embed(title="Koala!!!!")
        async with aiohttp.request("get","https://some-random-api.ml/img/koala") as res:
            x=json.loads(await res.text())
        res.close()
        em.set_image(url=x["link"])
        await ctx.send(embed=em)

    @commands.command()
    async def wink(self,ctx):
        em=em = discord.Embed(title=";)")
        async with aiohttp.request("get","https://some-random-api.ml/animu/wink") as res:
            x=json.loads(await res.text())
        res.close()
        em.set_image(url=x["link"])
        await ctx.send(embed=em)

    @commands.command()
    async def pika(self,ctx):
        em=em = discord.Embed(title="pika!")
        async with aiohttp.request("get","https://some-random-api.ml/img/pikachu") as res:
            x=json.loads(await res.text())
        res.close()
        em.set_image(url=x["link"])
        await ctx.send(embed=em)


##    @commands,command()
##    async def search(self, ctx,args):
##        x="https://www.google.co.in/search?q="+str(args)+"&rlz=1C1CHBF_enIN799IN799&oq=meems&aqs=chrome..69i57j0l5.806j0j7&sourceid=chrome&ie=UTF-8"
##        
        
        
def setup(bot):
    bot.add_cog(Net_Commands(bot))
