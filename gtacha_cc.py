import discord
from discord.ext import commands
import json
import aiohttp
import random

class Gatcha_cc:
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def roll(self, ctx, args):
        


def setup(bot):
    bot.add_cog(Gatcha_cc(bot))
