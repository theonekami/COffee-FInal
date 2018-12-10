import discord
from discord.ext import commands
import json
import aiohttp
import random
import gatchadata

class Gatcha_cc:
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def gatcha(self, ctx):
        current = gatchadata.gatchas[0]
        em = discord.Embed(title="###"+str(current.number)+current.name)
        em.add_field("Rarity:","Common",inline=False)
        em,add_field(" ",current.flavor)
        em.set_image(current.img)
        await ctx.send(embed= em)


def setup(bot):
    bot.add_cog(Gatcha_cc(bot))
