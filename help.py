import discord
from discord.ext import commands
import json
import aiohttp

class Helpe(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.group(name="help" , invoke_without_command=True)
    async def help(self,ctx):
        x= discord.Embed(title= "Help Subcommands")
        x.add_field(name="Utility",value="For your Rp , or just general life needs use !help utility", inline=False)
        x.add_field(name="Gaming",value="For your EPIC GAMING needs, use !help game", inline=False)
        x.add_field(name="Magic",value="For your Magic the gathering needs, use !help magic", inline=False)
        x.add_field(name="Image",value="For your cuteness needs, use !help img", inline=False)
        x.add_field(name="Meme",value="For some SUPER SECRET COMMANDS use !help img", inline=False)
        await ctx.send(embed=x)
    

    
def setup(bot):
    bot.add_cog(Helpe(bot))
