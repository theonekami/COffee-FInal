import discord
from discord.ext import commands
import json
import aiohttp


class Net_Commands:
    def __init__(self, bot):
        self.bot=bot


    @commands.command()
    async def cat(ctx):
        em = discord.Embed(title="Cat Pix")
        async with aiohttp.get("http://thecatapi.com/api/images/get") as res:
            em.set_image(url=res.url)
        res.close()
        await ctx.send(embed= em)

    @commands.command()
    async def dog(ctx):
        em = discord.Embed(title="Doggo Pix")
        async with aiohttp.get("https://dog.ceo/api/breeds/image/random") as res:
            x= json.loads(await res.text())
        res.close()
        em.set_image(url=x['message'])
        await ctx.send(embed= em)

def setup(bot):
    bot.add_cog(Net_Commands(bot))
